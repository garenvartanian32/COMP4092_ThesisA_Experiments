def predict(self, x):
        """
        Predict values for a single data point or an RDD of points
        using the model trained.
        """
        if isinstance(x, RDD):
            return x.map(lambda v: self.predict(v))

        x = _convert_to_vector(x)
        if self.numClasses == 2:
            margin = self.weights.dot(x) + self._intercept
            if margin > 0:
                prob = 1 / (1 + exp(-margin))
            else:
                exp_margin = exp(margin)
                prob = exp_margin / (1 + exp_margin)
            if self._threshold is None:
                return prob
            else:
                return 1 if prob > self._threshold else 0
        else:
            best_class = 0
            max_margin = 0.0
            if x.size + 1 == self._dataWithBiasSize:
                for i in range(0, self._numClasses - 1):
                    margin = x.dot(self._weightsMatrix[i][0:x.size]) + \
                        self._weightsMatrix[i][x.size]
                    if margin > max_margin:
                        max_margin = margin
                        best_class = i + 1
            else:
                for i in range(0, self._numClasses - 1):
                    margin = x.dot(self._weightsMatrix[i])
                    if margin > max_margin:
                        max_margin = margin
                        best_class = i + 1
            return best_class