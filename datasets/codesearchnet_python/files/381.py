def split(str, pattern, limit=-1):
    """
    Splits str around matches of the given pattern.

    :param str: a string expression to split
    :param pattern: a string representing a regular expression. The regex string should be
        a Java regular expression.
    :param limit: an integer which controls the number of times `pattern` is applied.

        * ``limit > 0``: The resulting array's length will not be more than `limit`, and the
                         resulting array's last entry will contain all input beyond the last
                         matched pattern.
        * ``limit <= 0``: `pattern` will be applied as many times as possible, and the resulting
                          array can be of any size.

    .. versionchanged:: 3.0
       `split` now takes an optional `limit` field. If not provided, default limit value is -1.

    >>> df = spark.createDataFrame([('oneAtwoBthreeC',)], ['s',])
    >>> df.select(split(df.s, '[ABC]', 2).alias('s')).collect()
    [Row(s=[u'one', u'twoBthreeC'])]
    >>> df.select(split(df.s, '[ABC]', -1).alias('s')).collect()
    [Row(s=[u'one', u'two', u'three', u''])]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.split(_to_java_column(str), pattern, limit))