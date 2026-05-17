def transform(self, vector):
        """
        Applies transformation on a vector or an RDD[Vector].

        .. note:: In Python, transform cannot currently be used within
            an RDD transformation or action.
            Call transform directly on the RDD instead.

        :param vector: Vector or RDD of Vector to be transformed.
        """
        if isinstance(vector, RDD):
            vector = vector.map(_convert_to_vector)
        else:
            vector = _convert_to_vector(vector)
        return self.call("transform", vector)