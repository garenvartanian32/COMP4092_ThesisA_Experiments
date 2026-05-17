def predict(self, x):
        """
        Predict values for a single data point or an RDD of points using
        the model trained.

        .. note:: In Python, predict cannot currently be used within an RDD
            transformation or action.
            Call predict directly on the RDD instead.
        """
        if isinstance(x, RDD):
            return self.call("predict", x.map(_convert_to_vector))

        else:
            return self.call("predict", _convert_to_vector(x))