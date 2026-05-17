def countByValue(self):
        """
        Return the count of each unique value in this RDD as a dictionary of
        (value, count) pairs.

        >>> sorted(sc.parallelize([1, 2, 1, 2, 2], 2).countByValue().items())
        [(1, 2), (2, 3)]
        """
        def countPartition(iterator):
            counts = defaultdict(int)
            for obj in iterator:
                counts[obj] += 1
            yield counts

        def mergeMaps(m1, m2):
            for k, v in m2.items():
                m1[k] += v
            return m1
        return self.mapPartitions(countPartition).reduce(mergeMaps)