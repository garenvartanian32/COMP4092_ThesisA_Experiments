def mapValues(self, f):
        """
        Pass each value in the key-value pair RDD through a map function
        without changing the keys; this also retains the original RDD's
        partitioning.

        >>> x = sc.parallelize([("a", ["apple", "banana", "lemon"]), ("b", ["grapes"])])
        >>> def f(x): return len(x)
        >>> x.mapValues(f).collect()
        [('a', 3), ('b', 1)]
        """
        map_values_fn = lambda kv: (kv[0], f(kv[1]))
        return self.map(map_values_fn, preservesPartitioning=True)