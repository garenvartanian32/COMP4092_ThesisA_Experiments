def window(self, windowDuration, slideDuration=None):
        """
        Return a new DStream in which each RDD contains all the elements in seen in a
        sliding window of time over this DStream.

        @param windowDuration: width of the window; must be a multiple of this DStream's
                              batching interval
        @param slideDuration:  sliding interval of the window (i.e., the interval after which
                              the new DStream will generate RDDs); must be a multiple of this
                              DStream's batching interval
        """
        self._validate_window_param(windowDuration, slideDuration)
        d = self._ssc._jduration(windowDuration)
        if slideDuration is None:
            return DStream(self._jdstream.window(d), self._ssc, self._jrdd_deserializer)
        s = self._ssc._jduration(slideDuration)
        return DStream(self._jdstream.window(d, s), self._ssc, self._jrdd_deserializer)