def computeSVD(self, k, computeU=False, rCond=1e-9):
        """
        Computes the singular value decomposition of the RowMatrix.

        The given row matrix A of dimension (m X n) is decomposed into
        U * s * V'T where

        * U: (m X k) (left singular vectors) is a RowMatrix whose
             columns are the eigenvectors of (A X A')
        * s: DenseVector consisting of square root of the eigenvalues
             (singular values) in descending order.
        * v: (n X k) (right singular vectors) is a Matrix whose columns
             are the eigenvectors of (A' X A)

        For more specific details on implementation, please refer
        the Scala documentation.

        :param k: Number of leading singular values to keep (`0 < k <= n`).
                  It might return less than k if there are numerically zero singular values
                  or there are not enough Ritz values converged before the maximum number of
                  Arnoldi update iterations is reached (in case that matrix A is ill-conditioned).
        :param computeU: Whether or not to compute U. If set to be
                         True, then U is computed by A * V * s^-1
        :param rCond: Reciprocal condition number. All singular values
                      smaller than rCond * s[0] are treated as zero
                      where s[0] is the largest singular value.
        :returns: :py:class:`SingularValueDecomposition`

        >>> rows = sc.parallelize([[3, 1, 1], [-1, 3, 1]])
        >>> rm = RowMatrix(rows)

        >>> svd_model = rm.computeSVD(2, True)
        >>> svd_model.U.rows.collect()
        [DenseVector([-0.7071, 0.7071]), DenseVector([-0.7071, -0.7071])]
        >>> svd_model.s
        DenseVector([3.4641, 3.1623])
        >>> svd_model.V
        DenseMatrix(3, 2, [-0.4082, -0.8165, -0.4082, 0.8944, -0.4472, 0.0], 0)
        """
        j_model = self._java_matrix_wrapper.call(
            "computeSVD", int(k), bool(computeU), float(rCond))
        return SingularValueDecomposition(j_model)