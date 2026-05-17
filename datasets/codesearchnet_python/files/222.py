def findFrequentSequentialPatterns(self, dataset):
        """
        .. note:: Experimental

        Finds the complete set of frequent sequential patterns in the input sequences of itemsets.

        :param dataset: A dataframe containing a sequence column which is
                        `ArrayType(ArrayType(T))` type, T is the item type for the input dataset.
        :return: A `DataFrame` that contains columns of sequence and corresponding frequency.
                 The schema of it will be:
                 - `sequence: ArrayType(ArrayType(T))` (T is the item type)
                 - `freq: Long`

        >>> from pyspark.ml.fpm import PrefixSpan
        >>> from pyspark.sql import Row
        >>> df = sc.parallelize([Row(sequence=[[1, 2], [3]]),
        ...                      Row(sequence=[[1], [3, 2], [1, 2]]),
        ...                      Row(sequence=[[1, 2], [5]]),
        ...                      Row(sequence=[[6]])]).toDF()
        >>> prefixSpan = PrefixSpan(minSupport=0.5, maxPatternLength=5)
        >>> prefixSpan.findFrequentSequentialPatterns(df).sort("sequence").show(truncate=False)
        +----------+----+
        |sequence  |freq|
        +----------+----+
        |[[1]]     |3   |
        |[[1], [3]]|2   |
        |[[1, 2]]  |3   |
        |[[2]]     |3   |
        |[[3]]     |2   |
        +----------+----+

        .. versionadded:: 2.4.0
        """
        self._transfer_params_to_java()
        jdf = self._java_obj.findFrequentSequentialPatterns(dataset._jdf)
        return DataFrame(jdf, dataset.sql_ctx)