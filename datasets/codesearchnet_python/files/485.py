def fromML(mat):
        """
        Convert a matrix from the new mllib-local representation.
        This does NOT copy the data; it copies references.

        :param mat: a :py:class:`pyspark.ml.linalg.Matrix`
        :return: a :py:class:`pyspark.mllib.linalg.Matrix`

        .. versionadded:: 2.0.0
        """
        if isinstance(mat, newlinalg.DenseMatrix):
            return DenseMatrix(mat.numRows, mat.numCols, mat.values, mat.isTransposed)
        elif isinstance(mat, newlinalg.SparseMatrix):
            return SparseMatrix(mat.numRows, mat.numCols, mat.colPtrs, mat.rowIndices,
                                mat.values, mat.isTransposed)
        else:
            raise TypeError("Unsupported matrix type %s" % type(mat))