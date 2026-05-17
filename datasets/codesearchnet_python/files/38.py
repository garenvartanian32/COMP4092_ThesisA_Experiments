def _spill(self):
        """
        dump already partitioned data into disks.

        It will dump the data in batch for better performance.
        """
        global MemoryBytesSpilled, DiskBytesSpilled
        path = self._get_spill_dir(self.spills)
        if not os.path.exists(path):
            os.makedirs(path)

        used_memory = get_used_memory()
        if not self.pdata:
            # The data has not been partitioned, it will iterator the
            # dataset once, write them into different files, has no
            # additional memory. It only called when the memory goes
            # above limit at the first time.

            # open all the files for writing
            streams = [open(os.path.join(path, str(i)), 'wb')
                       for i in range(self.partitions)]

            for k, v in self.data.items():
                h = self._partition(k)
                # put one item in batch, make it compatible with load_stream
                # it will increase the memory if dump them in batch
                self.serializer.dump_stream([(k, v)], streams[h])

            for s in streams:
                DiskBytesSpilled += s.tell()
                s.close()

            self.data.clear()
            self.pdata.extend([{} for i in range(self.partitions)])

        else:
            for i in range(self.partitions):
                p = os.path.join(path, str(i))
                with open(p, "wb") as f:
                    # dump items in batch
                    self.serializer.dump_stream(iter(self.pdata[i].items()), f)
                self.pdata[i].clear()
                DiskBytesSpilled += os.path.getsize(p)

        self.spills += 1
        gc.collect()  # release the memory as much as possible
        MemoryBytesSpilled += max(used_memory - get_used_memory(), 0) << 20