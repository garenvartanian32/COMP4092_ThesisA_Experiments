def countByValueAndWindow(self, windowDuration, slideDuration, numPartitions=None):
        """
        Return a new DStream in which each RDD contains the count of distinct elements in
        RDDs in a sliding window over this DStream.

        @param windowDuration: width of the window; must be a multiple of this DStream's
                              batching interval
        @param slideDuration:  sliding interval of the window (i.e., the interval after which
                              the new DStream will generate RDDs); must be a multiple of this
                              DStream's batching interval
        @param numPartitions:  number of partitions of each RDD in the new DStream.
        """
        keyed = self.map(lambda x: (x, 1))
        counted = keyed.reduceByKeyAndWindow(operator.add, operator.sub,
                                             windowDuration, slideDuration, numPartitions)
        return counted.filter(lambda kv: kv[1] > 0)