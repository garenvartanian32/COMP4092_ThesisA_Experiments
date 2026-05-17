def cogroup(self, other, numPartitions=None):
        """
        Return a new DStream by applying 'cogroup' between RDDs of this
        DStream and `other` DStream.

        Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
        """
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism
        return self.transformWith(lambda a, b: a.cogroup(b, numPartitions), other)