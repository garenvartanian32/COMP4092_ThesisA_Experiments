def summary(self, featuresCol, weightCol=None):
        """
        Returns an aggregate object that contains the summary of the column with the requested
        metrics.

        :param featuresCol:
         a column that contains features Vector object.
        :param weightCol:
         a column that contains weight value. Default weight is 1.0.
        :return:
         an aggregate column that contains the statistics. The exact content of this
         structure is determined during the creation of the builder.
        """
        featuresCol, weightCol = Summarizer._check_param(featuresCol, weightCol)
        return Column(self._java_obj.summary(featuresCol._jc, weightCol._jc))