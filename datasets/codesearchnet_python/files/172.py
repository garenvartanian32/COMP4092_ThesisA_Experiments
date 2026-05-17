def train(cls, rdd, k, maxIterations=100, runs=1, initializationMode="k-means||",
              seed=None, initializationSteps=2, epsilon=1e-4, initialModel=None):
        """
        Train a k-means clustering model.

        :param rdd:
          Training points as an `RDD` of `Vector` or convertible
          sequence types.
        :param k:
          Number of clusters to create.
        :param maxIterations:
          Maximum number of iterations allowed.
          (default: 100)
        :param runs:
          This param has no effect since Spark 2.0.0.
        :param initializationMode:
          The initialization algorithm. This can be either "random" or
          "k-means||".
          (default: "k-means||")
        :param seed:
          Random seed value for cluster initialization. Set as None to
          generate seed based on system time.
          (default: None)
        :param initializationSteps:
          Number of steps for the k-means|| initialization mode.
          This is an advanced setting -- the default of 2 is almost
          always enough.
          (default: 2)
        :param epsilon:
          Distance threshold within which a center will be considered to
          have converged. If all centers move less than this Euclidean
          distance, iterations are stopped.
          (default: 1e-4)
        :param initialModel:
          Initial cluster centers can be provided as a KMeansModel object
          rather than using the random or k-means|| initializationModel.
          (default: None)
        """
        if runs != 1:
            warnings.warn("The param `runs` has no effect since Spark 2.0.0.")
        clusterInitialModel = []
        if initialModel is not None:
            if not isinstance(initialModel, KMeansModel):
                raise Exception("initialModel is of "+str(type(initialModel))+". It needs "
                                "to be of <type 'KMeansModel'>")
            clusterInitialModel = [_convert_to_vector(c) for c in initialModel.clusterCenters]
        model = callMLlibFunc("trainKMeansModel", rdd.map(_convert_to_vector), k, maxIterations,
                              runs, initializationMode, seed, initializationSteps, epsilon,
                              clusterInitialModel)
        centers = callJavaFunc(rdd.context, model.clusterCenters)
        return KMeansModel([c.toArray() for c in centers])