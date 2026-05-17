def foldByKey(self, zeroValue, func, numPartitions=None, partitionFunc=portable_hash):
        """
        Merge the values for each key using an associative function "func"
        and a neutral "zeroValue" which may be added to the result an
        arbitrary number of times, and must not change the result
        (e.g., 0 for addition, or 1 for multiplication.).

        >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
        >>> from operator import add
        >>> sorted(rdd.foldByKey(0, add).collect())
        [('a', 2), ('b', 1)]
        """
        def createZero():
            return copy.deepcopy(zeroValue)

        return self.combineByKey(lambda v: func(createZero(), v), func, func, numPartitions,
                                 partitionFunc)