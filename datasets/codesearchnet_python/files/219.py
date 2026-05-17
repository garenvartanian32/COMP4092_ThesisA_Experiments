def updateStateByKey(self, updateFunc, numPartitions=None, initialRDD=None):
        """
        Return a new "state" DStream where the state for each key is updated by applying
        the given function on the previous state of the key and the new values of the key.

        @param updateFunc: State update function. If this function returns None, then
                           corresponding state key-value pair will be eliminated.
        """
        if numPartitions is None:
            numPartitions = self._sc.defaultParallelism

        if initialRDD and not isinstance(initialRDD, RDD):
            initialRDD = self._sc.parallelize(initialRDD)

        def reduceFunc(t, a, b):
            if a is None:
                g = b.groupByKey(numPartitions).mapValues(lambda vs: (list(vs), None))
            else:
                g = a.cogroup(b.partitionBy(numPartitions), numPartitions)
                g = g.mapValues(lambda ab: (list(ab[1]), list(ab[0])[0] if len(ab[0]) else None))
            state = g.mapValues(lambda vs_s: updateFunc(vs_s[0], vs_s[1]))
            return state.filter(lambda k_v: k_v[1] is not None)

        jreduceFunc = TransformFunction(self._sc, reduceFunc,
                                        self._sc.serializer, self._jrdd_deserializer)
        if initialRDD:
            initialRDD = initialRDD._reserialize(self._jrdd_deserializer)
            dstream = self._sc._jvm.PythonStateDStream(self._jdstream.dstream(), jreduceFunc,
                                                       initialRDD._jrdd)
        else:
            dstream = self._sc._jvm.PythonStateDStream(self._jdstream.dstream(), jreduceFunc)

        return DStream(dstream.asJavaDStream(), self._ssc, self._sc.serializer)