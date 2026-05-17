def rdd(self):
        """Returns the content as an :class:`pyspark.RDD` of :class:`Row`.
        """
        if self._lazy_rdd is None:
            jrdd = self._jdf.javaToPython()
            self._lazy_rdd = RDD(jrdd, self.sql_ctx._sc, BatchedSerializer(PickleSerializer()))
        return self._lazy_rdd