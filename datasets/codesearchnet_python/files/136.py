def transform(self, document):
        """
        Transforms the input document (list of terms) to term frequency
        vectors, or transform the RDD of document to RDD of term
        frequency vectors.
        """
        if isinstance(document, RDD):
            return document.map(self.transform)

        freq = {}
        for term in document:
            i = self.indexOf(term)
            freq[i] = 1.0 if self.binary else freq.get(i, 0) + 1.0
        return Vectors.sparse(self.numFeatures, freq.items())