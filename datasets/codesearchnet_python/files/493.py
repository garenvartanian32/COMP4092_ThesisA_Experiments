def findSynonymsArray(self, word, num):
        """
        Find "num" number of words closest in similarity to "word".
        word can be a string or vector representation.
        Returns an array with two fields word and similarity (which
        gives the cosine similarity).
        """
        if not isinstance(word, basestring):
            word = _convert_to_vector(word)
        tuples = self._java_obj.findSynonymsArray(word, num)
        return list(map(lambda st: (st._1(), st._2()), list(tuples)))