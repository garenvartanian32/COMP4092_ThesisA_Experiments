def train(cls, rdd, k, maxIterations=100, initMode="random"):
        r"""
        :param rdd:
          An RDD of (i, j, s\ :sub:`ij`\) tuples representing the
          affinity matrix, which is the matrix A in the PIC paper.  The
          similarity s\ :sub:`ij`\ must be nonnegative.  This is a symmetric
          matrix and hence s\ :sub:`ij`\ = s\ :sub:`ji`\  For any (i, j) with
          nonzero similarity, there should be either (i, j, s\ :sub:`ij`\) or
          (j, i, s\ :sub:`ji`\) in the input.  Tuples with i = j are ignored,
          because it is assumed s\ :sub:`ij`\ = 0.0.
        :param k:
          Number of clusters.
        :param maxIterations:
          Maximum number of iterations of the PIC algorithm.
          (default: 100)
        :param initMode:
          Initialization mode. This can be either "random" to use
          a random vector as vertex properties, or "degree" to use
          normalized sum similarities.
          (default: "random")
        """
        model = callMLlibFunc("trainPowerIterationClusteringModel",
                              rdd.map(_convert_to_vector), int(k), int(maxIterations), initMode)
        return PowerIterationClusteringModel(model)