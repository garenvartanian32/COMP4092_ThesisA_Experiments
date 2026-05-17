def toLocalIterator(self):
        """
        Return an iterator that contains all of the elements in this RDD.
        The iterator will consume as much memory as the largest partition in this RDD.

        >>> rdd = sc.parallelize(range(10))
        >>> [x for x in rdd.toLocalIterator()]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        with SCCallSiteSync(self.context) as css:
            sock_info = self.ctx._jvm.PythonRDD.toLocalIteratorAndServe(self._jrdd.rdd())
        return _load_from_socket(sock_info, self._jrdd_deserializer)