def saveAsTextFiles(self, prefix, suffix=None):
        """
        Save each RDD in this DStream as at text file, using string
        representation of elements.
        """
        def saveAsTextFile(t, rdd):
            path = rddToFileName(prefix, suffix, t)
            try:
                rdd.saveAsTextFile(path)
            except Py4JJavaError as e:
                # after recovered from checkpointing, the foreachRDD may
                # be called twice
                if 'FileAlreadyExistsException' not in str(e):
                    raise
        return self.foreachRDD(saveAsTextFile)