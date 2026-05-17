def predict(self, x):
        """
        Predict values for a single data point or an RDD of points
        using the model trained.
        """
        if isinstance(x, RDD):
            return x.map(lambda v: self.predict(v))

        x = _convert_to_vector(x)
        margin = self.weights.dot(x) + self.intercept
        if self._threshold is None:
            return margin
        else:
            return 1 if margin > self._threshold else 0