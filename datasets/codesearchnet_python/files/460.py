def blocks(self):
        """
        The RDD of sub-matrix blocks
        ((blockRowIndex, blockColIndex), sub-matrix) that form this
        distributed matrix.

        >>> mat = BlockMatrix(
        ...     sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                     ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))]), 3, 2)
        >>> blocks = mat.blocks
        >>> blocks.first()
        ((0, 0), DenseMatrix(3, 2, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 0))

        """
        # We use DataFrames for serialization of sub-matrix blocks
        # from Java, so we first convert the RDD of blocks to a
        # DataFrame on the Scala/Java side. Then we map each Row in
        # the DataFrame back to a sub-matrix block on this side.
        blocks_df = callMLlibFunc("getMatrixBlocks", self._java_matrix_wrapper._java_model)
        blocks = blocks_df.rdd.map(lambda row: ((row[0][0], row[0][1]), row[1]))
        return blocks