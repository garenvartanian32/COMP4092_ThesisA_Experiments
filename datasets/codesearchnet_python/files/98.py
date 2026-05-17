def aggregateByKey(self, zeroValue, seqFunc, combFunc, numPartitions=None,
                       partitionFunc=portable_hash):
        """
        Aggregate the values of each key, using given combine functions and a neutral
        "zero value". This function can return a different result type, U, than the type
        of the values in this RDD, V. Thus, we need one operation for merging a V into
        a U and one operation for merging two U's, The former operation is used for merging
        values within a partition, and the latter is used for merging values between
        partitions. To avoid memory allocation, both of these functions are
        allowed to modify and return their first argument instead of creating a new U.
        """
        def createZero():
            return copy.deepcopy(zeroValue)

        return self.combineByKey(
            lambda v: seqFunc(createZero(), v), seqFunc, combFunc, numPartitions, partitionFunc)