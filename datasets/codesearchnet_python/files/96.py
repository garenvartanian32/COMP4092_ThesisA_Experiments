def partitionBy(self, numPartitions, partitionFunc=portable_hash):
        """
        Return a copy of the RDD partitioned using the specified partitioner.

        >>> pairs = sc.parallelize([1, 2, 3, 4, 2, 4, 1]).map(lambda x: (x, x))
        >>> sets = pairs.partitionBy(2).glom().collect()
        >>> len(set(sets[0]).intersection(set(sets[1])))
        0
        """
        if numPartitions is None:
            numPartitions = self._defaultReducePartitions()
        partitioner = Partitioner(numPartitions, partitionFunc)
        if self.partitioner == partitioner:
            return self

        # Transferring O(n) objects to Java is too expensive.
        # Instead, we'll form the hash buckets in Python,
        # transferring O(numPartitions) objects to Java.
        # Each object is a (splitNumber, [objects]) pair.
        # In order to avoid too huge objects, the objects are
        # grouped into chunks.
        outputSerializer = self.ctx._unbatched_serializer

        limit = (_parse_memory(self.ctx._conf.get(
            "spark.python.worker.memory", "512m")) / 2)

        def add_shuffle_key(split, iterator):

            buckets = defaultdict(list)
            c, batch = 0, min(10 * numPartitions, 1000)

            for k, v in iterator:
                buckets[partitionFunc(k) % numPartitions].append((k, v))
                c += 1

                # check used memory and avg size of chunk of objects
                if (c % 1000 == 0 and get_used_memory() > limit
                        or c > batch):
                    n, size = len(buckets), 0
                    for split in list(buckets.keys()):
                        yield pack_long(split)
                        d = outputSerializer.dumps(buckets[split])
                        del buckets[split]
                        yield d
                        size += len(d)

                    avg = int(size / n) >> 20
                    # let 1M < avg < 10M
                    if avg < 1:
                        batch *= 1.5
                    elif avg > 10:
                        batch = max(int(batch / 1.5), 1)
                    c = 0

            for split, items in buckets.items():
                yield pack_long(split)
                yield outputSerializer.dumps(items)

        keyed = self.mapPartitionsWithIndex(add_shuffle_key, preservesPartitioning=True)
        keyed._bypass_serializer = True
        with SCCallSiteSync(self.context) as css:
            pairRDD = self.ctx._jvm.PairwiseRDD(
                keyed._jrdd.rdd()).asJavaPairRDD()
            jpartitioner = self.ctx._jvm.PythonPartitioner(numPartitions,
                                                           id(partitionFunc))
        jrdd = self.ctx._jvm.PythonRDD.valueOfPair(pairRDD.partitionBy(jpartitioner))
        rdd = RDD(jrdd, self.ctx, BatchedSerializer(outputSerializer))
        rdd.partitioner = partitioner
        return rdd