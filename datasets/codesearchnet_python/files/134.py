def fit(self, data):
        """
        Returns a ChiSquared feature selector.

        :param data: an `RDD[LabeledPoint]` containing the labeled dataset
                     with categorical features. Real-valued features will be
                     treated as categorical for each distinct value.
                     Apply feature discretizer before using this function.
        """
        jmodel = callMLlibFunc("fitChiSqSelector", self.selectorType, self.numTopFeatures,
                               self.percentile, self.fpr, self.fdr, self.fwe, data)
        return ChiSqSelectorModel(jmodel)