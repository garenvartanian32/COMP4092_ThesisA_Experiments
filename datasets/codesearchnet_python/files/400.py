def array_repeat(col, count):
    """
    Collection function: creates an array containing a column repeated count times.

    >>> df = spark.createDataFrame([('ab',)], ['data'])
    >>> df.select(array_repeat(df.data, 3).alias('r')).collect()
    [Row(r=[u'ab', u'ab', u'ab'])]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.array_repeat(_to_java_column(col), count))