def add(self, other):
        """
        Adds two block matrices together. The matrices must have the
        same size and matching `rowsPerBlock` and `colsPerBlock` values.
        If one of the sub matrix blocks that are being added is a
        SparseMatrix, the resulting sub matrix block will also be a
        SparseMatrix, even if it is being added to a DenseMatrix. If
        two dense sub matrix blocks are added, the output block will
        also be a DenseMatrix.

        >>> dm1 = Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])
        >>> dm2 = Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12])
        >>> sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 1, 2], [7, 11, 12])
        >>> blocks1 = sc.parallelize([((0, 0), dm1), ((1, 0), dm2)])
        >>> blocks2 = sc.parallelize([((0, 0), dm1), ((1, 0), dm2)])
        >>> blocks3 = sc.parallelize([((0, 0), sm), ((1, 0), dm2)])
        >>> mat1 = BlockMatrix(blocks1, 3, 2)
        >>> mat2 = BlockMatrix(blocks2, 3, 2)
        >>> mat3 = BlockMatrix(blocks3, 3, 2)

        >>> mat1.add(mat2).toLocalMatrix()
        DenseMatrix(6, 2, [2.0, 4.0, 6.0, 14.0, 16.0, 18.0, 8.0, 10.0, 12.0, 20.0, 22.0, 24.0], 0)

        >>> mat1.add(mat3).toLocalMatrix()
        DenseMatrix(6, 2, [8.0, 2.0, 3.0, 14.0, 16.0, 18.0, 4.0, 16.0, 18.0, 20.0, 22.0, 24.0], 0)
        """
        if not isinstance(other, BlockMatrix):
            raise TypeError("Other should be a BlockMatrix, got %s" % type(other))

        other_java_block_matrix = other._java_matrix_wrapper._java_model
        java_block_matrix = self._java_matrix_wrapper.call("add", other_java_block_matrix)
        return BlockMatrix(java_block_matrix, self.rowsPerBlock, self.colsPerBlock)