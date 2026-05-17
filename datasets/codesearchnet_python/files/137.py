def fit(self, dataset):
        """
        Computes the inverse document frequency.

        :param dataset: an RDD of term frequency vectors
        """
        if not isinstance(dataset, RDD):
            raise TypeError("dataset should be an RDD of term frequency vectors")
        jmodel = callMLlibFunc("fitIDF", self.minDocFreq, dataset.map(_convert_to_vector))
        return IDFModel(jmodel)