def saveAsSequenceFile(self, path, compressionCodecClass=None):
        """
        Output a Python RDD of key-value pairs (of form C{RDD[(K, V)]}) to any Hadoop file
        system, using the L{org.apache.hadoop.io.Writable} types that we convert from the
        RDD's key and value types. The mechanism is as follows:

            1. Pyrolite is used to convert pickled Python RDD into RDD of Java objects.
            2. Keys and values of this Java RDD are converted to Writables and written out.

        :param path: path to sequence file
        :param compressionCodecClass: (None by default)
        """
        pickledRDD = self._pickled()
        self.ctx._jvm.PythonRDD.saveAsSequenceFile(pickledRDD._jrdd, True,
                                                   path, compressionCodecClass)