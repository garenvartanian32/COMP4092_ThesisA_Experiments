def collect(self):
        """
        Return a list that contains all of the elements in this RDD.

        .. note:: This method should only be used if the resulting array is expected
            to be small, as all the data is loaded into the driver's memory.
        """
        with SCCallSiteSync(self.context) as css:
            sock_info = self.ctx._jvm.PythonRDD.collectAndServe(self._jrdd.rdd())
        return list(_load_from_socket(sock_info, self._jrdd_deserializer))