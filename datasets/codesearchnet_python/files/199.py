def partitionBy(self, numPartitions, partitionFunc=portable_hash):
        """
        Return a copy of the DStream in which each RDD are partitioned
        using the specified partitioner.
        """
        return self.transform(lambda rdd: rdd.partitionBy(numPartitions, partitionFunc))