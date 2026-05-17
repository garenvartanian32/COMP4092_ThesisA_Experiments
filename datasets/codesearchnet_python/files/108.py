def zipWithIndex(self):
        """
        Zips this RDD with its element indices.

        The ordering is first based on the partition index and then the
        ordering of items within each partition. So the first item in
        the first partition gets index 0, and the last item in the last
        partition receives the largest index.

        This method needs to trigger a spark job when this RDD contains
        more than one partitions.

        >>> sc.parallelize(["a", "b", "c", "d"], 3).zipWithIndex().collect()
        [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
        """
        starts = [0]
        if self.getNumPartitions() > 1:
            nums = self.mapPartitions(lambda it: [sum(1 for i in it)]).collect()
            for i in range(len(nums) - 1):
                starts.append(starts[-1] + nums[i])

        def func(k, it):
            for i, v in enumerate(it, starts[k]):
                yield v, i

        return self.mapPartitionsWithIndex(func)