def subtract(self, other, numPartitions=None):
        """
        Return each value in C{self} that is not contained in C{other}.

        >>> x = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 3)])
        >>> y = sc.parallelize([("a", 3), ("c", None)])
        >>> sorted(x.subtract(y).collect())
        [('a', 1), ('b', 4), ('b', 5)]
        """
        # note: here 'True' is just a placeholder
        rdd = other.map(lambda x: (x, True))
        return self.map(lambda x: (x, True)).subtractByKey(rdd, numPartitions).keys()