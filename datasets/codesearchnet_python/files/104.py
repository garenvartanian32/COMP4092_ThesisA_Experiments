def subtractByKey(self, other, numPartitions=None):
        """
        Return each (key, value) pair in C{self} that has no pair with matching
        key in C{other}.

        >>> x = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 2)])
        >>> y = sc.parallelize([("a", 3), ("c", None)])
        >>> sorted(x.subtractByKey(y).collect())
        [('b', 4), ('b', 5)]
        """
        def filter_func(pair):
            key, (val1, val2) = pair
            return val1 and not val2
        return self.cogroup(other, numPartitions).filter(filter_func).flatMapValues(lambda x: x[0])