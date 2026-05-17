def generateLinearRDD(sc, nexamples, nfeatures, eps,
                          nParts=2, intercept=0.0):
        """
        Generate an RDD of LabeledPoints.
        """
        return callMLlibFunc(
            "generateLinearRDDWrapper", sc, int(nexamples), int(nfeatures),
            float(eps), int(nParts), float(intercept))