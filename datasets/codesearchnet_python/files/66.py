def repartitionAndSortWithinPartitions(self, numPartitions=None, partitionFunc=portable_hash,
                                           ascending=True, keyfunc=lambda x: x):
        """
        Repartition the RDD according to the given partitioner and, within each resulting partition,
        sort records by their keys.

        >>> rdd = sc.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
        >>> rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, True)
        >>> rdd2.glom().collect()
        [[(0, 5), (0, 8), (2, 6)], [(1, 3), (3, 8), (3, 8)]]
        """
        if numPartitions is None:
            numPartitions = self._defaultReducePartitions()

        memory = _parse_memory(self.ctx._conf.get("spark.python.worker.memory", "512m"))
        serializer = self._jrdd_deserializer

        def sortPartition(iterator):
            sort = ExternalSorter(memory * 0.9, serializer).sorted
            return iter(sort(iterator, key=lambda k_v: keyfunc(k_v[0]), reverse=(not ascending)))

        return self.partitionBy(numPartitions, partitionFunc).mapPartitions(sortPartition, True)