def multiply(self, matrix):
        """
        Multiply this matrix by a local dense matrix on the right.

        :param matrix: a local dense matrix whose number of rows must match the number of columns
                       of this matrix
        :returns: :py:class:`IndexedRowMatrix`

        >>> mat = IndexedRowMatrix(sc.parallelize([(0, (0, 1)), (1, (2, 3))]))
        >>> mat.multiply(DenseMatrix(2, 2, [0, 2, 1, 3])).rows.collect()
        [IndexedRow(0, [2.0,3.0]), IndexedRow(1, [6.0,11.0])]
        """
        if not isinstance(matrix, DenseMatrix):
            raise ValueError("Only multiplication with DenseMatrix "
                             "is supported.")
        return IndexedRowMatrix(self._java_matrix_wrapper.call("multiply", matrix))