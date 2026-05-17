def train(self, rdd, k=4, maxIterations=20, minDivisibleClusterSize=1.0, seed=-1888008604):
        """
        Runs the bisecting k-means algorithm return the model.

        :param rdd:
          Training points as an `RDD` of `Vector` or convertible
          sequence types.
        :param k:
          The desired number of leaf clusters. The actual number could
          be smaller if there are no divisible leaf clusters.
          (default: 4)
        :param maxIterations:
          Maximum number of iterations allowed to split clusters.
          (default: 20)
        :param minDivisibleClusterSize:
          Minimum number of points (if >= 1.0) or the minimum proportion
          of points (if < 1.0) of a divisible cluster.
          (default: 1)
        :param seed:
          Random seed value for cluster initialization.
          (default: -1888008604 from classOf[BisectingKMeans].getName.##)
        """
        java_model = callMLlibFunc(
            "trainBisectingKMeans", rdd.map(_convert_to_vector),
            k, maxIterations, minDivisibleClusterSize, seed)
        return BisectingKMeansModel(java_model)