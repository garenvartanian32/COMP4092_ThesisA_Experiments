def approxSimilarityJoin(self, datasetA, datasetB, threshold, distCol="distCol"):
        """
        Join two datasets to approximately find all pairs of rows whose distance are smaller than
        the threshold. If the :py:attr:`outputCol` is missing, the method will transform the data;
        if the :py:attr:`outputCol` exists, it will use that. This allows caching of the
        transformed data when necessary.

        :param datasetA: One of the datasets to join.
        :param datasetB: Another dataset to join.
        :param threshold: The threshold for the distance of row pairs.
        :param distCol: Output column for storing the distance between each pair of rows. Use
                        "distCol" as default value if it's not specified.
        :return: A joined dataset containing pairs of rows. The original rows are in columns
                 "datasetA" and "datasetB", and a column "distCol" is added to show the distance
                 between each pair.
        """
        threshold = TypeConverters.toFloat(threshold)
        return self._call_java("approxSimilarityJoin", datasetA, datasetB, threshold, distCol)