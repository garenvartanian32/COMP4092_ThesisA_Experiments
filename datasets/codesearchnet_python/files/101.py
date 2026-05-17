def flatMapValues(self, f):
        """
        Pass each value in the key-value pair RDD through a flatMap function
        without changing the keys; this also retains the original RDD's
        partitioning.

        >>> x = sc.parallelize([("a", ["x", "y", "z"]), ("b", ["p", "r"])])
        >>> def f(x): return x
        >>> x.flatMapValues(f).collect()
        [('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')]
        """
        flat_map_fn = lambda kv: ((kv[0], x) for x in f(kv[1]))
        return self.flatMap(flat_map_fn, preservesPartitioning=True)