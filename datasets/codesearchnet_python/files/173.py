def train(cls, rdd, k, convergenceTol=1e-3, maxIterations=100, seed=None, initialModel=None):
        """
        Train a Gaussian Mixture clustering model.

        :param rdd:
          Training points as an `RDD` of `Vector` or convertible
          sequence types.
        :param k:
          Number of independent Gaussians in the mixture model.
        :param convergenceTol:
          Maximum change in log-likelihood at which convergence is
          considered to have occurred.
          (default: 1e-3)
        :param maxIterations:
          Maximum number of iterations allowed.
          (default: 100)
        :param seed:
          Random seed for initial Gaussian distribution. Set as None to
          generate seed based on system time.
          (default: None)
        :param initialModel:
          Initial GMM starting point, bypassing the random
          initialization.
          (default: None)
        """
        initialModelWeights = None
        initialModelMu = None
        initialModelSigma = None
        if initialModel is not None:
            if initialModel.k != k:
                raise Exception("Mismatched cluster count, initialModel.k = %s, however k = %s"
                                % (initialModel.k, k))
            initialModelWeights = list(initialModel.weights)
            initialModelMu = [initialModel.gaussians[i].mu for i in range(initialModel.k)]
            initialModelSigma = [initialModel.gaussians[i].sigma for i in range(initialModel.k)]
        java_model = callMLlibFunc("trainGaussianMixtureModel", rdd.map(_convert_to_vector),
                                   k, convergenceTol, maxIterations, seed,
                                   initialModelWeights, initialModelMu, initialModelSigma)
        return GaussianMixtureModel(java_model)