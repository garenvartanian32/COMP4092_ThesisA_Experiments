def reduceByKeyAndWindow(self, func, invFunc, windowDuration, slideDuration=None,
                             numPartitions=None, filterFunc=None):
        """
        Return a new DStream by applying incremental `reduceByKey` over a sliding window.

        The reduced value of over a new window is calculated using the old window's reduce value :
         1. reduce the new values that entered the window (e.g., adding new counts)
         2. "inverse reduce" the old values that left the window (e.g., subtracting old counts)

        `invFunc` can be None, then it will reduce all the RDDs in window, could be slower
        than having `invFunc`.

        @param func:           associative and commutative reduce function
        @param invFunc:        inverse function of `reduceFunc`
        @param windowDuration: width of the window; must be a multiple of this DStream's
                              batching interval
        @param slideDuration:  sliding interval of the window (i.e., the interval after which
                              the new DStream will generate RDDs); must be a multiple of this
                              DStream's batching interval
        @param numPartitions:  number of partitions of each RDD in the new DStream.
        @param filterFunc:     function to filter expired key-value pairs;
                              only pairs that satisfy the function are retained
                              set this to null if you do not want to filter
        """
        self._validate_window_param(windowDuration, slideDuration)
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism

        reduced = self.reduceByKey(func, numPartitions)

        if invFunc:
            def reduceFunc(t, a, b):
                b = b.reduceByKey(func, numPartitions)
                r = a.union(b).reduceByKey(func, numPartitions) if a else b
                if filterFunc:
                    r = r.filter(filterFunc)
                return r

            def invReduceFunc(t, a, b):
                b = b.reduceByKey(func, numPartitions)
                joined = a.leftOuterJoin(b, numPartitions)
                return joined.mapValues(lambda kv: invFunc(kv[0], kv[1])
                                        if kv[1] is not None else kv[0])

            jreduceFunc = TransformFunction(self._sc, reduceFunc, reduced._jrdd_deserializer)
            jinvReduceFunc = TransformFunction(self._sc, invReduceFunc, reduced._jrdd_deserializer)
            if slideDuration is None:
                slideDuration = self._slideDuration
            dstream = self._sc._jvm.PythonReducedWindowedDStream(
                reduced._jdstream.dstream(),
                jreduceFunc, jinvReduceFunc,
                self._ssc._jduration(windowDuration),
                self._ssc._jduration(slideDuration))
            return DStream(dstream.asJavaDStream(), self._ssc, self._sc.serializer)
        else:
            return reduced.window(windowDuration, slideDuration).reduceByKey(func, numPartitions)