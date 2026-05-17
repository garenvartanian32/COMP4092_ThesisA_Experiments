def stats(self):
        """
        Return a L{StatCounter} object that captures the mean, variance
        and count of the RDD's elements in one operation.
        """
        def redFunc(left_counter, right_counter):
            return left_counter.mergeStats(right_counter)

        return self.mapPartitions(lambda i: [StatCounter(i)]).reduce(redFunc)