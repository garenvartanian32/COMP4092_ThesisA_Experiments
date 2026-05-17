def coalesce(self, numPartitions, shuffle=False):
        """
        Return a new RDD that is reduced into `numPartitions` partitions.

        >>> sc.parallelize([1, 2, 3, 4, 5], 3).glom().collect()
        [[1], [2, 3], [4, 5]]
        >>> sc.parallelize([1, 2, 3, 4, 5], 3).coalesce(1).glom().collect()
        [[1, 2, 3, 4, 5]]
        """
        if shuffle:
            # Decrease the batch size in order to distribute evenly the elements across output
            # partitions. Otherwise, repartition will possibly produce highly skewed partitions.
            batchSize = min(10, self.ctx._batchSize or 1024)
            ser = BatchedSerializer(PickleSerializer(), batchSize)
            selfCopy = self._reserialize(ser)
            jrdd_deserializer = selfCopy._jrdd_deserializer
            jrdd = selfCopy._jrdd.coalesce(numPartitions, shuffle)
        else:
            jrdd_deserializer = self._jrdd_deserializer
            jrdd = self._jrdd.coalesce(numPartitions, shuffle)
        return RDD(jrdd, self.ctx, jrdd_deserializer)