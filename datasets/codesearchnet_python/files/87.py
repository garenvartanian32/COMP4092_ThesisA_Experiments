def takeOrdered(self, num, key=None):
        """
        Get the N elements from an RDD ordered in ascending order or as
        specified by the optional key function.

        .. note:: this method should only be used if the resulting array is expected
            to be small, as all the data is loaded into the driver's memory.

        >>> sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7]).takeOrdered(6)
        [1, 2, 3, 4, 5, 6]
        >>> sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7], 2).takeOrdered(6, key=lambda x: -x)
        [10, 9, 7, 6, 5, 4]
        """

        def merge(a, b):
            return heapq.nsmallest(num, a + b, key)

        return self.mapPartitions(lambda it: [heapq.nsmallest(num, it, key)]).reduce(merge)