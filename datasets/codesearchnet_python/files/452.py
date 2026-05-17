def tallSkinnyQR(self, computeQ=False):
        """
        Compute the QR decomposition of this RowMatrix.

        The implementation is designed to optimize the QR decomposition
        (factorization) for the RowMatrix of a tall and skinny shape.

        Reference:
         Paul G. Constantine, David F. Gleich. "Tall and skinny QR
         factorizations in MapReduce architectures"
         ([[https://doi.org/10.1145/1996092.1996103]])

        :param: computeQ: whether to computeQ
        :return: QRDecomposition(Q: RowMatrix, R: Matrix), where
                 Q = None if computeQ = false.

        >>> rows = sc.parallelize([[3, -6], [4, -8], [0, 1]])
        >>> mat = RowMatrix(rows)
        >>> decomp = mat.tallSkinnyQR(True)
        >>> Q = decomp.Q
        >>> R = decomp.R

        >>> # Test with absolute values
        >>> absQRows = Q.rows.map(lambda row: abs(row.toArray()).tolist())
        >>> absQRows.collect()
        [[0.6..., 0.0], [0.8..., 0.0], [0.0, 1.0]]

        >>> # Test with absolute values
        >>> abs(R.toArray()).tolist()
        [[5.0, 10.0], [0.0, 1.0]]
        """
        decomp = JavaModelWrapper(self._java_matrix_wrapper.call("tallSkinnyQR", computeQ))
        if computeQ:
            java_Q = decomp.call("Q")
            Q = RowMatrix(java_Q)
        else:
            Q = None
        R = decomp.call("R")
        return QRDecomposition(Q, R)