def to_date(col, format=None):
    """Converts a :class:`Column` of :class:`pyspark.sql.types.StringType` or
    :class:`pyspark.sql.types.TimestampType` into :class:`pyspark.sql.types.DateType`
    using the optionally specified format. Specify formats according to
    `DateTimeFormatter <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html>`_. # noqa
    By default, it follows casting rules to :class:`pyspark.sql.types.DateType` if the format
    is omitted (equivalent to ``col.cast("date")``).

    >>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
    >>> df.select(to_date(df.t).alias('date')).collect()
    [Row(date=datetime.date(1997, 2, 28))]

    >>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
    >>> df.select(to_date(df.t, 'yyyy-MM-dd HH:mm:ss').alias('date')).collect()
    [Row(date=datetime.date(1997, 2, 28))]
    """
    sc = SparkContext._active_spark_context
    if format is None:
        jc = sc._jvm.functions.to_date(_to_java_column(col))
    else:
        jc = sc._jvm.functions.to_date(_to_java_column(col), format)
    return Column(jc)