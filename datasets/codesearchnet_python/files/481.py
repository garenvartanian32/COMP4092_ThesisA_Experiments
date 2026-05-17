def asML(self):
        """
        Convert this matrix to the new mllib-local representation.
        This does NOT copy the data; it copies references.

        :return: :py:class:`pyspark.ml.linalg.DenseMatrix`

        .. versionadded:: 2.0.0
        """
        return newlinalg.DenseMatrix(self.numRows, self.numCols, self.values, self.isTransposed)