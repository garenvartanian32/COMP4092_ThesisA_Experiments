def reduceByKey(self, func, numPartitions=None):
        """
        Return a new DStream by applying reduceByKey to each RDD.
        """
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism
        return self.combineByKey(lambda x: x, func, func, numPartitions)