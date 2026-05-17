def countByValue(self):
        """
        Return a new DStream in which each RDD contains the counts of each
        distinct value in each RDD of this DStream.
        """
        return self.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y)