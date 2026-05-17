def multiply(self, matrix):
        """
        Multiply this matrix by a local dense matrix on the right.

        :param matrix: a local dense matrix whose number of rows must match the number of columns
                       of this matrix
        :returns: :py:class:`RowMatrix`

        >>> rm = RowMatrix(sc.parallelize([[0, 1], [2, 3]]))
        >>> rm.multiply(DenseMatrix(2, 2, [0, 2, 1, 3])).rows.collect()
        [DenseVector([2.0, 3.0]), DenseVector([6.0, 11.0])]
        """
        if not isinstance(matrix, DenseMatrix):
            raise ValueError("Only multiplication with DenseMatrix "
                             "is supported.")
        j_model = self._java_matrix_wrapper.call("multiply", matrix)
        return RowMatrix(j_model)