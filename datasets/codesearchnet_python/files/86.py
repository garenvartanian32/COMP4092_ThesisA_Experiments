def top(self, num, key=None):
        """
        Get the top N elements from an RDD.

        .. note:: This method should only be used if the resulting array is expected
            to be small, as all the data is loaded into the driver's memory.

        .. note:: It returns the list sorted in descending order.

        >>> sc.parallelize([10, 4, 2, 12, 3]).top(1)
        [12]
        >>> sc.parallelize([2, 3, 4, 5, 6], 2).top(2)
        [6, 5]
        >>> sc.parallelize([10, 4, 2, 12, 3]).top(3, key=str)
        [4, 3, 2]
        """
        def topIterator(iterator):
            yield heapq.nlargest(num, iterator, key=key)

        def merge(a, b):
            return heapq.nlargest(num, a + b, key=key)

        return self.mapPartitions(topIterator).reduce(merge)