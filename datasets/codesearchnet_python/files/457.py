def toBlockMatrix(self, rowsPerBlock=1024, colsPerBlock=1024):
        """
        Convert this matrix to a BlockMatrix.

        :param rowsPerBlock: Number of rows that make up each block.
                             The blocks forming the final rows are not
                             required to have the given number of rows.
        :param colsPerBlock: Number of columns that make up each block.
                             The blocks forming the final columns are not
                             required to have the given number of columns.

        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(6, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows).toBlockMatrix()

        >>> # This IndexedRowMatrix will have 7 effective rows, due to
        >>> # the highest row index being 6, and the ensuing
        >>> # BlockMatrix will have 7 rows as well.
        >>> print(mat.numRows())
        7

        >>> print(mat.numCols())
        3
        """
        java_block_matrix = self._java_matrix_wrapper.call("toBlockMatrix",
                                                           rowsPerBlock,
                                                           colsPerBlock)
        return BlockMatrix(java_block_matrix, rowsPerBlock, colsPerBlock)