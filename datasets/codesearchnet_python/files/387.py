def array_join(col, delimiter, null_replacement=None):
    """
    Concatenates the elements of `column` using the `delimiter`. Null values are replaced with
    `null_replacement` if set, otherwise they are ignored.

    >>> df = spark.createDataFrame([(["a", "b", "c"],), (["a", None],)], ['data'])
    >>> df.select(array_join(df.data, ",").alias("joined")).collect()
    [Row(joined=u'a,b,c'), Row(joined=u'a')]
    >>> df.select(array_join(df.data, ",", "NULL").alias("joined")).collect()
    [Row(joined=u'a,b,c'), Row(joined=u'a,NULL')]
    """
    sc = SparkContext._active_spark_context
    if null_replacement is None:
        return Column(sc._jvm.functions.array_join(_to_java_column(col), delimiter))
    else:
        return Column(sc._jvm.functions.array_join(
            _to_java_column(col), delimiter, null_replacement))