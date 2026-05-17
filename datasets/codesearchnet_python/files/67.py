def sortByKey(self, ascending=True, numPartitions=None, keyfunc=lambda x: x):
        """
        Sorts this RDD, which is assumed to consist of (key, value) pairs.

        >>> tmp = [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
        >>> sc.parallelize(tmp).sortByKey().first()
        ('1', 3)
        >>> sc.parallelize(tmp).sortByKey(True, 1).collect()
        [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
        >>> sc.parallelize(tmp).sortByKey(True, 2).collect()
        [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
        >>> tmp2 = [('Mary', 1), ('had', 2), ('a', 3), ('little', 4), ('lamb', 5)]
        >>> tmp2.extend([('whose', 6), ('fleece', 7), ('was', 8), ('white', 9)])
        >>> sc.parallelize(tmp2).sortByKey(True, 3, keyfunc=lambda k: k.lower()).collect()
        [('a', 3), ('fleece', 7), ('had', 2), ('lamb', 5),...('white', 9), ('whose', 6)]
        """
        if numPartitions is None:
            numPartitions = self._defaultReducePartitions()

        memory = self._memory_limit()
        serializer = self._jrdd_deserializer

        def sortPartition(iterator):
            sort = ExternalSorter(memory * 0.9, serializer).sorted
            return iter(sort(iterator, key=lambda kv: keyfunc(kv[0]), reverse=(not ascending)))

        if numPartitions == 1:
            if self.getNumPartitions() > 1:
                self = self.coalesce(1)
            return self.mapPartitions(sortPartition, True)

        # first compute the boundary of each part via sampling: we want to partition
        # the key-space into bins such that the bins have roughly the same
        # number of (key, value) pairs falling into them
        rddSize = self.count()
        if not rddSize:
            return self  # empty RDD
        maxSampleSize = numPartitions * 20.0  # constant from Spark's RangePartitioner
        fraction = min(maxSampleSize / max(rddSize, 1), 1.0)
        samples = self.sample(False, fraction, 1).map(lambda kv: kv[0]).collect()
        samples = sorted(samples, key=keyfunc)

        # we have numPartitions many parts but one of the them has
        # an implicit boundary
        bounds = [samples[int(len(samples) * (i + 1) / numPartitions)]
                  for i in range(0, numPartitions - 1)]

        def rangePartitioner(k):
            p = bisect.bisect_left(bounds, keyfunc(k))
            if ascending:
                return p
            else:
                return numPartitions - 1 - p

        return self.partitionBy(numPartitions, rangePartitioner).mapPartitions(sortPartition, True)