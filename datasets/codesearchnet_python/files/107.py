def zip(self, other):
        """
        Zips this RDD with another one, returning key-value pairs with the
        first element in each RDD second element in each RDD, etc. Assumes
        that the two RDDs have the same number of partitions and the same
        number of elements in each partition (e.g. one was made through
        a map on the other).

        >>> x = sc.parallelize(range(0,5))
        >>> y = sc.parallelize(range(1000, 1005))
        >>> x.zip(y).collect()
        [(0, 1000), (1, 1001), (2, 1002), (3, 1003), (4, 1004)]
        """
        def get_batch_size(ser):
            if isinstance(ser, BatchedSerializer):
                return ser.batchSize
            return 1  # not batched

        def batch_as(rdd, batchSize):
            return rdd._reserialize(BatchedSerializer(PickleSerializer(), batchSize))

        my_batch = get_batch_size(self._jrdd_deserializer)
        other_batch = get_batch_size(other._jrdd_deserializer)
        if my_batch != other_batch or not my_batch:
            # use the smallest batchSize for both of them
            batchSize = min(my_batch, other_batch)
            if batchSize <= 0:
                # auto batched or unlimited
                batchSize = 100
            other = batch_as(other, batchSize)
            self = batch_as(self, batchSize)

        if self.getNumPartitions() != other.getNumPartitions():
            raise ValueError("Can only zip with RDD which has the same number of partitions")

        # There will be an Exception in JVM if there are different number
        # of items in each partitions.
        pairRDD = self._jrdd.zip(other._jrdd)
        deserializer = PairDeserializer(self._jrdd_deserializer,
                                        other._jrdd_deserializer)
        return RDD(pairRDD, self.ctx, deserializer)