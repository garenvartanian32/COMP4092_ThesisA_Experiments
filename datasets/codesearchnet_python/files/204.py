def groupByKey(self, numPartitions=None):
        """
        Return a new DStream by applying groupByKey on each RDD.
        """
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism
        return self.transform(lambda rdd: rdd.groupByKey(numPartitions))