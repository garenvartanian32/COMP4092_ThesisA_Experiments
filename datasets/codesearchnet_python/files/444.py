def generateLinearInput(intercept, weights, xMean, xVariance,
                            nPoints, seed, eps):
        """
        :param: intercept bias factor, the term c in X'w + c
        :param: weights   feature vector, the term w in X'w + c
        :param: xMean     Point around which the data X is centered.
        :param: xVariance Variance of the given data
        :param: nPoints   Number of points to be generated
        :param: seed      Random Seed
        :param: eps       Used to scale the noise. If eps is set high,
                          the amount of gaussian noise added is more.

        Returns a list of LabeledPoints of length nPoints
        """
        weights = [float(weight) for weight in weights]
        xMean = [float(mean) for mean in xMean]
        xVariance = [float(var) for var in xVariance]
        return list(callMLlibFunc(
            "generateLinearInputWrapper", float(intercept), weights, xMean,
            xVariance, int(nPoints), int(seed), float(eps)))