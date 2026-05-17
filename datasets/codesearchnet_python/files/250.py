def sampleBy(self, col, fractions, seed=None):
        """
        Returns a stratified sample without replacement based on the
        fraction given on each stratum.

        :param col: column that defines strata
        :param fractions:
            sampling fraction for each stratum. If a stratum is not
            specified, we treat its fraction as zero.
        :param seed: random seed
        :return: a new DataFrame that represents the stratified sample

        >>> from pyspark.sql.functions import col
        >>> dataset = sqlContext.range(0, 100).select((col("id") % 3).alias("key"))
        >>> sampled = dataset.sampleBy("key", fractions={0: 0.1, 1: 0.2}, seed=0)
        >>> sampled.groupBy("key").count().orderBy("key").show()
        +---+-----+
        |key|count|
        +---+-----+
        |  0|    3|
        |  1|    6|
        +---+-----+
        >>> dataset.sampleBy(col("key"), fractions={2: 1.0}, seed=0).count()
        33

        .. versionchanged:: 3.0
           Added sampling by a column of :class:`Column`
        """
        if isinstance(col, basestring):
            col = Column(col)
        elif not isinstance(col, Column):
            raise ValueError("col must be a string or a column, but got %r" % type(col))
        if not isinstance(fractions, dict):
            raise ValueError("fractions must be a dict but got %r" % type(fractions))
        for k, v in fractions.items():
            if not isinstance(k, (float, int, long, basestring)):
                raise ValueError("key must be float, int, long, or string, but got %r" % type(k))
            fractions[k] = float(v)
        col = col._jc
        seed = seed if seed is not None else random.randint(0, sys.maxsize)
        return DataFrame(self._jdf.stat().sampleBy(col, self._jmap(fractions), seed), self.sql_ctx)