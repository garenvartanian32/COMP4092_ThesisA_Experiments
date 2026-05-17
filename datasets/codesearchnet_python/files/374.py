def format_string(format, *cols):
    """
    Formats the arguments in printf-style and returns the result as a string column.

    :param col: the column name of the numeric value to be formatted
    :param d: the N decimal places

    >>> df = spark.createDataFrame([(5, "hello")], ['a', 'b'])
    >>> df.select(format_string('%d %s', df.a, df.b).alias('v')).collect()
    [Row(v=u'5 hello')]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.format_string(format, _to_seq(sc, cols, _to_java_column)))