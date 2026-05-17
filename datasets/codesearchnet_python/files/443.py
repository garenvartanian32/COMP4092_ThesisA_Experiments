def convertVectorColumnsToML(dataset, *cols):
        """
        Converts vector columns in an input DataFrame from the
        :py:class:`pyspark.mllib.linalg.Vector` type to the new
        :py:class:`pyspark.ml.linalg.Vector` type under the `spark.ml`
        package.

        :param dataset:
          input dataset
        :param cols:
          a list of vector columns to be converted.
          New vector columns will be ignored. If unspecified, all old
          vector columns will be converted excepted nested ones.
        :return:
          the input dataset with old vector columns converted to the
          new vector type

        >>> import pyspark
        >>> from pyspark.mllib.linalg import Vectors
        >>> from pyspark.mllib.util import MLUtils
        >>> df = spark.createDataFrame(
        ...     [(0, Vectors.sparse(2, [1], [1.0]), Vectors.dense(2.0, 3.0))],
        ...     ["id", "x", "y"])
        >>> r1 = MLUtils.convertVectorColumnsToML(df).first()
        >>> isinstance(r1.x, pyspark.ml.linalg.SparseVector)
        True
        >>> isinstance(r1.y, pyspark.ml.linalg.DenseVector)
        True
        >>> r2 = MLUtils.convertVectorColumnsToML(df, "x").first()
        >>> isinstance(r2.x, pyspark.ml.linalg.SparseVector)
        True
        >>> isinstance(r2.y, pyspark.mllib.linalg.DenseVector)
        True
        """
        if not isinstance(dataset, DataFrame):
            raise TypeError("Input dataset must be a DataFrame but got {}.".format(type(dataset)))
        return callMLlibFunc("convertVectorColumnsToML", dataset, list(cols))