def zipWithUniqueId(self):
        """
        Zips this RDD with generated unique Long ids.

        Items in the kth partition will get ids k, n+k, 2*n+k, ..., where
        n is the number of partitions. So there may exist gaps, but this
        method won't trigger a spark job, which is different from
        L{zipWithIndex}

        >>> sc.parallelize(["a", "b", "c", "d", "e"], 3).zipWithUniqueId().collect()
        [('a', 0), ('b', 1), ('c', 4), ('d', 2), ('e', 5)]
        """
        n = self.getNumPartitions()

        def func(k, it):
            for i, v in enumerate(it):
                yield v, i * n + k

        return self.mapPartitionsWithIndex(func)