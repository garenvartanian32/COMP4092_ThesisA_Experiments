def foreachPartition(self, f):
        """
        Applies a function to each partition of this RDD.

        >>> def f(iterator):
        ...     for x in iterator:
        ...          print(x)
        >>> sc.parallelize([1, 2, 3, 4, 5]).foreachPartition(f)
        """
        def func(it):
            r = f(it)
            try:
                return iter(r)
            except TypeError:
                return iter([])
        self.mapPartitions(func).count()