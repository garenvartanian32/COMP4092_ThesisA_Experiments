def sortBy(self, keyfunc, ascending=True, numPartitions=None):
        """
        Sorts this RDD by the given keyfunc

        >>> tmp = [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
        >>> sc.parallelize(tmp).sortBy(lambda x: x[0]).collect()
        [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
        >>> sc.parallelize(tmp).sortBy(lambda x: x[1]).collect()
        [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
        """
        return self.keyBy(keyfunc).sortByKey(ascending, numPartitions).values()