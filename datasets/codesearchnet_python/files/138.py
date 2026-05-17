def findSynonyms(self, word, num):
        """
        Find synonyms of a word

        :param word: a word or a vector representation of word
        :param num: number of synonyms to find
        :return: array of (word, cosineSimilarity)

        .. note:: Local use only
        """
        if not isinstance(word, basestring):
            word = _convert_to_vector(word)
        words, similarity = self.call("findSynonyms", word, num)
        return zip(words, similarity)