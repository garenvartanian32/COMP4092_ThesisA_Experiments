def _spill(self):
        """
        dump already partitioned data into disks.
        """
        global MemoryBytesSpilled, DiskBytesSpilled
        path = self._get_spill_dir(self.spills)
        if not os.path.exists(path):
            os.makedirs(path)

        used_memory = get_used_memory()
        if not self.pdata:
            # The data has not been partitioned, it will iterator the
            # data once, write them into different files, has no
            # additional memory. It only called when the memory goes
            # above limit at the first time.

            # open all the files for writing
            streams = [open(os.path.join(path, str(i)), 'wb')
                       for i in range(self.partitions)]

            # If the number of keys is small, then the overhead of sort is small
            # sort them before dumping into disks
            self._sorted = len(self.data) < self.SORT_KEY_LIMIT
            if self._sorted:
                self.serializer = self.flattened_serializer()
                for k in sorted(self.data.keys()):
                    h = self._partition(k)
                    self.serializer.dump_stream([(k, self.data[k])], streams[h])
            else:
                for k, v in self.data.items():
                    h = self._partition(k)
                    self.serializer.dump_stream([(k, v)], streams[h])

            for s in streams:
                DiskBytesSpilled += s.tell()
                s.close()

            self.data.clear()
            # self.pdata is cached in `mergeValues` and `mergeCombiners`
            self.pdata.extend([{} for i in range(self.partitions)])

        else:
            for i in range(self.partitions):
                p = os.path.join(path, str(i))
                with open(p, "wb") as f:
                    # dump items in batch
                    if self._sorted:
                        # sort by key only (stable)
                        sorted_items = sorted(self.pdata[i].items(), key=operator.itemgetter(0))
                        self.serializer.dump_stream(sorted_items, f)
                    else:
                        self.serializer.dump_stream(self.pdata[i].items(), f)
                self.pdata[i].clear()
                DiskBytesSpilled += os.path.getsize(p)

        self.spills += 1
        gc.collect()  # release the memory as much as possible
        MemoryBytesSpilled += max(used_memory - get_used_memory(), 0) << 20