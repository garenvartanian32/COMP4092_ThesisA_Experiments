def saveAsPickleFile(self, path, batchSize=10):
        """
        Save this RDD as a SequenceFile of serialized objects. The serializer
        used is L{pyspark.serializers.PickleSerializer}, default batch size
        is 10.

        >>> tmpFile = NamedTemporaryFile(delete=True)
        >>> tmpFile.close()
        >>> sc.parallelize([1, 2, 'spark', 'rdd']).saveAsPickleFile(tmpFile.name, 3)
        >>> sorted(sc.pickleFile(tmpFile.name, 5).map(str).collect())
        ['1', '2', 'rdd', 'spark']
        """
        if batchSize == 0:
            ser = AutoBatchedSerializer(PickleSerializer())
        else:
            ser = BatchedSerializer(PickleSerializer(), batchSize)
        self._reserialize(ser)._jrdd.saveAsObjectFile(path)