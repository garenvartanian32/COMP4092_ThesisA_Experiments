def summary(self):
        """
        Gets summary (e.g. residuals, mse, r-squared ) of model on
        training set. An exception is thrown if
        `trainingSummary is None`.
        """
        if self.hasSummary:
            return LinearRegressionTrainingSummary(super(LinearRegressionModel, self).summary)
        else:
            raise RuntimeError("No training summary available for this %s" %
                               self.__class__.__name__)