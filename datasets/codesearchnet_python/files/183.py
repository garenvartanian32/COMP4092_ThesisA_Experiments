def describeTopics(self, maxTermsPerTopic=None):
        """Return the topics described by weighted terms.

        WARNING: If vocabSize and k are large, this can return a large object!

        :param maxTermsPerTopic:
          Maximum number of terms to collect for each topic.
          (default: vocabulary size)
        :return:
          Array over topics. Each topic is represented as a pair of
          matching arrays: (term indices, term weights in topic).
          Each topic's terms are sorted in order of decreasing weight.
        """
        if maxTermsPerTopic is None:
            topics = self.call("describeTopics")
        else:
            topics = self.call("describeTopics", maxTermsPerTopic)
        return topics