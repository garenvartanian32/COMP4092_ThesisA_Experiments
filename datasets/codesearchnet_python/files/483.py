def asML(self):
        """
        Convert this matrix to the new mllib-local representation.
        This does NOT copy the data; it copies references.

        :return: :py:class:`pyspark.ml.linalg.SparseMatrix`

        .. versionadded:: 2.0.0
        """
        return newlinalg.SparseMatrix(self.numRows, self.numCols, self.colPtrs, self.rowIndices,
                                      self.values, self.isTransposed)