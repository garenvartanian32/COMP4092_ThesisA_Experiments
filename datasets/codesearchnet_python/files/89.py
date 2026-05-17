def saveAsNewAPIHadoopDataset(self, conf, keyConverter=None, valueConverter=None):
        """
        Output a Python RDD of key-value pairs (of form C{RDD[(K, V)]}) to any Hadoop file
        system, using the new Hadoop OutputFormat API (mapreduce package). Keys/values are
        converted for output using either user specified converters or, by default,
        L{org.apache.spark.api.python.JavaToWritableConverter}.

        :param conf: Hadoop job configuration, passed in as a dict
        :param keyConverter: (None by default)
        :param valueConverter: (None by default)
        """
        jconf = self.ctx._dictToJavaMap(conf)
        pickledRDD = self._pickled()
        self.ctx._jvm.PythonRDD.saveAsHadoopDataset(pickledRDD._jrdd, True, jconf,
                                                    keyConverter, valueConverter, True)