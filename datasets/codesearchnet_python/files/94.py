def reduceByKey(self, func, numPartitions=None, partitionFunc=portable_hash):
        """
        Merge the values for each key using an associative and commutative reduce function.

        This will also perform the merging locally on each mapper before
        sending results to a reducer, similarly to a "combiner" in MapReduce.

        Output will be partitioned with C{numPartitions} partitions, or
        the default parallelism level if C{numPartitions} is not specified.
        Default partitioner is hash-partition.

        >>> from operator import add
        >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
        >>> sorted(rdd.reduceByKey(add).collect())
        [('a', 2), ('b', 1)]
        """
        return self.combineByKey(lambda x: x, func, func, numPartitions, partitionFunc)