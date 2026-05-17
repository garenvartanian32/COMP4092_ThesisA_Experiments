def metrics(*metrics):
        """
        Given a list of metrics, provides a builder that it turns computes metrics from a column.

        See the documentation of [[Summarizer]] for an example.

        The following metrics are accepted (case sensitive):
         - mean: a vector that contains the coefficient-wise mean.
         - variance: a vector tha contains the coefficient-wise variance.
         - count: the count of all vectors seen.
         - numNonzeros: a vector with the number of non-zeros for each coefficients
         - max: the maximum for each coefficient.
         - min: the minimum for each coefficient.
         - normL2: the Euclidean norm for each coefficient.
         - normL1: the L1 norm of each coefficient (sum of the absolute values).

        :param metrics:
         metrics that can be provided.
        :return:
         an object of :py:class:`pyspark.ml.stat.SummaryBuilder`

        Note: Currently, the performance of this interface is about 2x~3x slower then using the RDD
        interface.
        """
        sc = SparkContext._active_spark_context
        js = JavaWrapper._new_java_obj("org.apache.spark.ml.stat.Summarizer.metrics",
                                       _to_seq(sc, metrics))
        return SummaryBuilder(js)