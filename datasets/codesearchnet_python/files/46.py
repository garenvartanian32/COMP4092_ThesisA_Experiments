def _merge_sorted_items(self, index):
        """ load a partition from disk, then sort and group by key """
        def load_partition(j):
            path = self._get_spill_dir(j)
            p = os.path.join(path, str(index))
            with open(p, 'rb', 65536) as f:
                for v in self.serializer.load_stream(f):
                    yield v

        disk_items = [load_partition(j) for j in range(self.spills)]

        if self._sorted:
            # all the partitions are already sorted
            sorted_items = heapq.merge(disk_items, key=operator.itemgetter(0))

        else:
            # Flatten the combined values, so it will not consume huge
            # memory during merging sort.
            ser = self.flattened_serializer()
            sorter = ExternalSorter(self.memory_limit, ser)
            sorted_items = sorter.sorted(itertools.chain(*disk_items),
                                         key=operator.itemgetter(0))
        return ((k, vs) for k, vs in GroupByKey(sorted_items))