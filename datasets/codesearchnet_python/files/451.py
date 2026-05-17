def columnSimilarities(self, threshold=0.0):
        """
        Compute similarities between columns of this matrix.

        The threshold parameter is a trade-off knob between estimate
        quality and computational cost.

        The default threshold setting of 0 guarantees deterministically
        correct results, but uses the brute-force approach of computing
        normalized dot products.

        Setting the threshold to positive values uses a sampling
        approach and incurs strictly less computational cost than the
        brute-force approach. However the similarities computed will
        be estimates.

        The sampling guarantees relative-error correctness for those
        pairs of columns that have similarity greater than the given
        similarity threshold.

        To describe the guarantee, we set some notation:
            * Let A be the smallest in magnitude non-zero element of
              this matrix.
            * Let B be the largest in magnitude non-zero element of
              this matrix.
            * Let L be the maximum number of non-zeros per row.

        For example, for {0,1} matrices: A=B=1.
        Another example, for the Netflix matrix: A=1, B=5

        For those column pairs that are above the threshold, the
        computed similarity is correct to within 20% relative error
        with probability at least 1 - (0.981)^10/B^

        The shuffle size is bounded by the *smaller* of the following
        two expressions:

            * O(n log(n) L / (threshold * A))
            * O(m L^2^)

        The latter is the cost of the brute-force approach, so for
        non-zero thresholds, the cost is always cheaper than the
        brute-force approach.

        :param: threshold: Set to 0 for deterministic guaranteed
                           correctness. Similarities above this
                           threshold are estimated with the cost vs
                           estimate quality trade-off described above.
        :return: An n x n sparse upper-triangular CoordinateMatrix of
                 cosine similarities between columns of this matrix.

        >>> rows = sc.parallelize([[1, 2], [1, 5]])
        >>> mat = RowMatrix(rows)

        >>> sims = mat.columnSimilarities()
        >>> sims.entries.first().value
        0.91914503...
        """
        java_sims_mat = self._java_matrix_wrapper.call("columnSimilarities", float(threshold))
        return CoordinateMatrix(java_sims_mat)