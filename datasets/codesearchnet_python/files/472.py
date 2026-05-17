def asML(self):
        """
        Convert this vector to the new mllib-local representation.
        This does NOT copy the data; it copies references.

        :return: :py:class:`pyspark.ml.linalg.SparseVector`

        .. versionadded:: 2.0.0
        """
        return newlinalg.SparseVector(self.size, self.indices, self.values)