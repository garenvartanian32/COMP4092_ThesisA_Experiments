def summary(self):
        """
        Gets summary (e.g. residuals, deviance, pValues) of model on
        training set. An exception is thrown if
        `trainingSummary is None`.
        """
        if self.hasSummary:
            return GeneralizedLinearRegressionTrainingSummary(
                super(GeneralizedLinearRegressionModel, self).summary)
        else:
            raise RuntimeError("No training summary available for this %s" %
                               self.__class__.__name__)