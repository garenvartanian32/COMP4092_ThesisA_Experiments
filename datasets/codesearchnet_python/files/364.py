def date_trunc(format, timestamp):
    """
    Returns timestamp truncated to the unit specified by the format.

    :param format: 'year', 'yyyy', 'yy', 'month', 'mon', 'mm',
        'day', 'dd', 'hour', 'minute', 'second', 'week', 'quarter'

    >>> df = spark.createDataFrame([('1997-02-28 05:02:11',)], ['t'])
    >>> df.select(date_trunc('year', df.t).alias('year')).collect()
    [Row(year=datetime.datetime(1997, 1, 1, 0, 0))]
    >>> df.select(date_trunc('mon', df.t).alias('month')).collect()
    [Row(month=datetime.datetime(1997, 2, 1, 0, 0))]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.date_trunc(format, _to_java_column(timestamp)))