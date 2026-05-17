def countByWindow(self, windowDuration, slideDuration):
        """
        Return a new DStream in which each RDD has a single element generated
        by counting the number of elements in a window over this DStream.
        windowDuration and slideDuration are as defined in the window() operation.

        This is equivalent to window(windowDuration, slideDuration).count(),
        but will be more efficient if window is large.
        """
        return self.map(lambda x: 1).reduceByWindow(operator.add, operator.sub,
                                                    windowDuration, slideDuration)