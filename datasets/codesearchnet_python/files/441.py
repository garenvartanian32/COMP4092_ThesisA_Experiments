def loadLabeledPoints(sc, path, minPartitions=None):
        """
        Load labeled points saved using RDD.saveAsTextFile.

        :param sc: Spark context
        :param path: file or directory path in any Hadoop-supported file
                     system URI
        :param minPartitions: min number of partitions
        @return: labeled data stored as an RDD of LabeledPoint

        >>> from tempfile import NamedTemporaryFile
        >>> from pyspark.mllib.util import MLUtils
        >>> from pyspark.mllib.regression import LabeledPoint
        >>> examples = [LabeledPoint(1.1, Vectors.sparse(3, [(0, -1.23), (2, 4.56e-7)])),
        ...             LabeledPoint(0.0, Vectors.dense([1.01, 2.02, 3.03]))]
        >>> tempFile = NamedTemporaryFile(delete=True)
        >>> tempFile.close()
        >>> sc.parallelize(examples, 1).saveAsTextFile(tempFile.name)
        >>> MLUtils.loadLabeledPoints(sc, tempFile.name).collect()
        [LabeledPoint(1.1, (3,[0,2],[-1.23,4.56e-07])), LabeledPoint(0.0, [1.01,2.02,3.03])]
        """
        minPartitions = minPartitions or min(sc.defaultParallelism, 2)
        return callMLlibFunc("loadLabeledPoints", sc, path, minPartitions)