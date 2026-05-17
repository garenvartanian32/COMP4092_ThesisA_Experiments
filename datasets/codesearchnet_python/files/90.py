def saveAsNewAPIHadoopFile(self, path, outputFormatClass, keyClass=None, valueClass=None,
                               keyConverter=None, valueConverter=None, conf=None):
        """
        Output a Python RDD of key-value pairs (of form C{RDD[(K, V)]}) to any Hadoop file
        system, using the new Hadoop OutputFormat API (mapreduce package). Key and value types
        will be inferred if not specified. Keys and values are converted for output using either
        user specified converters or L{org.apache.spark.api.python.JavaToWritableConverter}. The
        C{conf} is applied on top of the base Hadoop conf associated with the SparkContext
        of this RDD to create a merged Hadoop MapReduce job configuration for saving the data.

        :param path: path to Hadoop file
        :param outputFormatClass: fully qualified classname of Hadoop OutputFormat
               (e.g. "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat")
        :param keyClass: fully qualified classname of key Writable class
               (e.g. "org.apache.hadoop.io.IntWritable", None by default)
        :param valueClass: fully qualified classname of value Writable class
               (e.g. "org.apache.hadoop.io.Text", None by default)
        :param keyConverter: (None by default)
        :param valueConverter: (None by default)
        :param conf: Hadoop job configuration, passed in as a dict (None by default)
        """
        jconf = self.ctx._dictToJavaMap(conf)
        pickledRDD = self._pickled()
        self.ctx._jvm.PythonRDD.saveAsNewAPIHadoopFile(pickledRDD._jrdd, True, path,
                                                       outputFormatClass,
                                                       keyClass, valueClass,
                                                       keyConverter, valueConverter, jconf)