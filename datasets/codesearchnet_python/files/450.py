def train(cls, data, isotonic=True):
        """
        Train an isotonic regression model on the given data.

        :param data:
          RDD of (label, feature, weight) tuples.
        :param isotonic:
          Whether this is isotonic (which is default) or antitonic.
          (default: True)
        """
        boundaries, predictions = callMLlibFunc("trainIsotonicRegressionModel",
                                                data.map(_convert_to_vector), bool(isotonic))
        return IsotonicRegressionModel(boundaries.toArray(), predictions.toArray(), isotonic)