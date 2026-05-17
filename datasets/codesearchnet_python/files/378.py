def locate(substr, str, pos=1):
    """
    Locate the position of the first occurrence of substr in a string column, after position pos.

    .. note:: The position is not zero based, but 1 based index. Returns 0 if substr
        could not be found in str.

    :param substr: a string
    :param str: a Column of :class:`pyspark.sql.types.StringType`
    :param pos: start position (zero based)

    >>> df = spark.createDataFrame([('abcd',)], ['s',])
    >>> df.select(locate('b', df.s, 1).alias('s')).collect()
    [Row(s=2)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.locate(substr, _to_java_column(str), pos))