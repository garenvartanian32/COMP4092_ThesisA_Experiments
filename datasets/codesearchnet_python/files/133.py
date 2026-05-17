def fit(self, dataset):
        """
        Computes the mean and variance and stores as a model to be used
        for later scaling.

        :param dataset: The data used to compute the mean and variance
                     to build the transformation model.
        :return: a StandardScalarModel
        """
        dataset = dataset.map(_convert_to_vector)
        jmodel = callMLlibFunc("fitStandardScaler", self.withMean, self.withStd, dataset)
        return StandardScalerModel(jmodel)