def fromML(vec):
        """
        Convert a vector from the new mllib-local representation.
        This does NOT copy the data; it copies references.

        :param vec: a :py:class:`pyspark.ml.linalg.Vector`
        :return: a :py:class:`pyspark.mllib.linalg.Vector`

        .. versionadded:: 2.0.0
        """
        if isinstance(vec, newlinalg.DenseVector):
            return DenseVector(vec.array)
        elif isinstance(vec, newlinalg.SparseVector):
            return SparseVector(vec.size, vec.indices, vec.values)
        else:
            raise TypeError("Unsupported vector type %s" % type(vec))