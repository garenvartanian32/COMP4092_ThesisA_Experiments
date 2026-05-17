def combineByKey(self, createCombiner, mergeValue, mergeCombiners,
                     numPartitions=None):
        """
        Return a new DStream by applying combineByKey to each RDD.
        """
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism

        def func(rdd):
            return rdd.combineByKey(createCombiner, mergeValue, mergeCombiners, numPartitions)
        return self.transform(func)