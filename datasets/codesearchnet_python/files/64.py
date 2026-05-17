def union(self, other):
        """
        Return the union of this RDD and another one.

        >>> rdd = sc.parallelize([1, 1, 2, 3])
        >>> rdd.union(rdd).collect()
        [1, 1, 2, 3, 1, 1, 2, 3]
        """
        if self._jrdd_deserializer == other._jrdd_deserializer:
            rdd = RDD(self._jrdd.union(other._jrdd), self.ctx,
                      self._jrdd_deserializer)
        else:
            # These RDDs contain data in different serialized formats, so we
            # must normalize them to the default serializer.
            self_copy = self._reserialize()
            other_copy = other._reserialize()
            rdd = RDD(self_copy._jrdd.union(other_copy._jrdd), self.ctx,
                      self.ctx.serializer)
        if (self.partitioner == other.partitioner and
                self.getNumPartitions() == rdd.getNumPartitions()):
            rdd.partitioner = self.partitioner
        return rdd