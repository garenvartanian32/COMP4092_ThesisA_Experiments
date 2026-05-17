def transform(self, vector):
        """
        Computes the Hadamard product of the vector.
        """
        if isinstance(vector, RDD):
            vector = vector.map(_convert_to_vector)

        else:
            vector = _convert_to_vector(vector)
        return callMLlibFunc("elementwiseProductVector", self.scalingVector, vector)