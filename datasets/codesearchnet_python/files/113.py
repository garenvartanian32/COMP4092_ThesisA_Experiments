def _to_java_object_rdd(self):
        """ Return a JavaRDD of Object by unpickling

        It will convert each Python object into Java object by Pyrolite, whenever the
        RDD is serialized in batch or not.
        """
        rdd = self._pickled()
        return self.ctx._jvm.SerDeUtil.pythonToJava(rdd._jrdd, True)