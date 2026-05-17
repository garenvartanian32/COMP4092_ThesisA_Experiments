def mapPartitionsWithSplit(self, f, preservesPartitioning=False):
        """
        Deprecated: use mapPartitionsWithIndex instead.

        Return a new RDD by applying a function to each partition of this RDD,
        while tracking the index of the original partition.

        >>> rdd = sc.parallelize([1, 2, 3, 4], 4)
        >>> def f(splitIndex, iterator): yield splitIndex
        >>> rdd.mapPartitionsWithSplit(f).sum()
        6
        """
        warnings.warn("mapPartitionsWithSplit is deprecated; "
                      "use mapPartitionsWithIndex instead", DeprecationWarning, stacklevel=2)
        return self.mapPartitionsWithIndex(f, preservesPartitioning)