def distinct(self, numPartitions=None):
        """
        Return a new RDD containing the distinct elements in this RDD.

        >>> sorted(sc.parallelize([1, 1, 2, 3]).distinct().collect())
        [1, 2, 3]
        """
        return self.map(lambda x: (x, None)) \
                   .reduceByKey(lambda x, _: x, numPartitions) \
                   .map(lambda x: x[0])