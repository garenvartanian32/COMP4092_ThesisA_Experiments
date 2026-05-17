def combineByKey(self, createCombiner, mergeValue, mergeCombiners,
                     numPartitions=None, partitionFunc=portable_hash):
        """
        Generic function to combine the elements for each key using a custom
        set of aggregation functions.

        Turns an RDD[(K, V)] into a result of type RDD[(K, C)], for a "combined
        type" C.

        Users provide three functions:

            - C{createCombiner}, which turns a V into a C (e.g., creates
              a one-element list)
            - C{mergeValue}, to merge a V into a C (e.g., adds it to the end of
              a list)
            - C{mergeCombiners}, to combine two C's into a single one (e.g., merges
              the lists)

        To avoid memory allocation, both mergeValue and mergeCombiners are allowed to
        modify and return their first argument instead of creating a new C.

        In addition, users can control the partitioning of the output RDD.

        .. note:: V and C can be different -- for example, one might group an RDD of type
            (Int, Int) into an RDD of type (Int, List[Int]).

        >>> x = sc.parallelize([("a", 1), ("b", 1), ("a", 2)])
        >>> def to_list(a):
        ...     return [a]
        ...
        >>> def append(a, b):
        ...     a.append(b)
        ...     return a
        ...
        >>> def extend(a, b):
        ...     a.extend(b)
        ...     return a
        ...
        >>> sorted(x.combineByKey(to_list, append, extend).collect())
        [('a', [1, 2]), ('b', [1])]
        """
        if numPartitions is None:
            numPartitions = self._defaultReducePartitions()

        serializer = self.ctx.serializer
        memory = self._memory_limit()
        agg = Aggregator(createCombiner, mergeValue, mergeCombiners)

        def combineLocally(iterator):
            merger = ExternalMerger(agg, memory * 0.9, serializer)
            merger.mergeValues(iterator)
            return merger.items()

        locally_combined = self.mapPartitions(combineLocally, preservesPartitioning=True)
        shuffled = locally_combined.partitionBy(numPartitions, partitionFunc)

        def _mergeCombiners(iterator):
            merger = ExternalMerger(agg, memory, serializer)
            merger.mergeCombiners(iterator)
            return merger.items()

        return shuffled.mapPartitions(_mergeCombiners, preservesPartitioning=True)