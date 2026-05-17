def fit(self, data):
        """
        Computes a [[PCAModel]] that contains the principal components of the input vectors.
        :param data: source vectors
        """
        jmodel = callMLlibFunc("fitPCA", self.k, data)
        return PCAModel(jmodel)