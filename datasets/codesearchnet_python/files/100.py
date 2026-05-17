def groupByKey(self, numPartitions=None, partitionFunc=portable_hash):
        """
        Group the values for each key in the RDD into a single sequence.
        Hash-partitions the resulting RDD with numPartitions partitions.

        .. note:: If you are grouping in order to perform an aggregation (such as a
            sum or average) over each key, using reduceByKey or aggregateByKey will
            provide much better performance.

        >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
        >>> sorted(rdd.groupByKey().mapValues(len).collect())
        [('a', 2), ('b', 1)]
        >>> sorted(rdd.groupByKey().mapValues(list).collect())
        [('a', [1, 1]), ('b', [1])]
        """
        def createCombiner(x):
            return [x]

        def mergeValue(xs, x):
            xs.append(x)
            return xs

        def mergeCombiners(a, b):
            a.extend(b)
            return a

        memory = self._memory_limit()
        serializer = self._jrdd_deserializer
        agg = Aggregator(createCombiner, mergeValue, mergeCombiners)

        def combine(iterator):
            merger = ExternalMerger(agg, memory * 0.9, serializer)
            merger.mergeValues(iterator)
            return merger.items()

        locally_combined = self.mapPartitions(combine, preservesPartitioning=True)
        shuffled = locally_combined.partitionBy(numPartitions, partitionFunc)

        def groupByKey(it):
            merger = ExternalGroupBy(agg, memory, serializer)
            merger.mergeCombiners(it)
            return merger.items()

        return shuffled.mapPartitions(groupByKey, True).mapValues(ResultIterable)