def flatMap(self, f, preservesPartitioning=False):
        """
        Return a new RDD by first applying a function to all elements of this
        RDD, and then flattening the results.

        >>> rdd = sc.parallelize([2, 3, 4])
        >>> sorted(rdd.flatMap(lambda x: range(1, x)).collect())
        [1, 1, 1, 2, 2, 3]
        >>> sorted(rdd.flatMap(lambda x: [(x, x), (x, x)]).collect())
        [(2, 2), (2, 2), (3, 3), (3, 3), (4, 4), (4, 4)]
        """
        def func(s, iterator):
            return chain.from_iterable(map(fail_on_stopiteration(f), iterator))
        return self.mapPartitionsWithIndex(func, preservesPartitioning)