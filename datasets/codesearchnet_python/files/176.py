def update(self, data, decayFactor, timeUnit):
        """Update the centroids, according to data

        :param data:
          RDD with new data for the model update.
        :param decayFactor:
          Forgetfulness of the previous centroids.
        :param timeUnit:
          Can be "batches" or "points". If points, then the decay factor
          is raised to the power of number of new points and if batches,
          then decay factor will be used as is.
        """
        if not isinstance(data, RDD):
            raise TypeError("Data should be of an RDD, got %s." % type(data))
        data = data.map(_convert_to_vector)
        decayFactor = float(decayFactor)
        if timeUnit not in ["batches", "points"]:
            raise ValueError(
                "timeUnit should be 'batches' or 'points', got %s." % timeUnit)
        vectorCenters = [_convert_to_vector(center) for center in self.centers]
        updatedModel = callMLlibFunc(
            "updateStreamingKMeansModel", vectorCenters, self._clusterWeights,
            data, decayFactor, timeUnit)
        self.centers = array(updatedModel[0])
        self._clusterWeights = list(updatedModel[1])
        return self