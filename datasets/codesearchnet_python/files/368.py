def from_utc_timestamp(timestamp, tz):
    """
    This is a common function for databases supporting TIMESTAMP WITHOUT TIMEZONE. This function
    takes a timestamp which is timezone-agnostic, and interprets it as a timestamp in UTC, and
    renders that timestamp as a timestamp in the given time zone.

    However, timestamp in Spark represents number of microseconds from the Unix epoch, which is not
    timezone-agnostic. So in Spark this function just shift the timestamp value from UTC timezone to
    the given timezone.

    This function may return confusing result if the input is a string with timezone, e.g.
    '2018-03-13T06:18:23+00:00'. The reason is that, Spark firstly cast the string to timestamp
    according to the timezone in the string, and finally display the result by converting the
    timestamp to string according to the session local timezone.

    :param timestamp: the column that contains timestamps
    :param tz: a string that has the ID of timezone, e.g. "GMT", "America/Los_Angeles", etc

    .. versionchanged:: 2.4
       `tz` can take a :class:`Column` containing timezone ID strings.

    >>> df = spark.createDataFrame([('1997-02-28 10:30:00', 'JST')], ['ts', 'tz'])
    >>> df.select(from_utc_timestamp(df.ts, "PST").alias('local_time')).collect()
    [Row(local_time=datetime.datetime(1997, 2, 28, 2, 30))]
    >>> df.select(from_utc_timestamp(df.ts, df.tz).alias('local_time')).collect()
    [Row(local_time=datetime.datetime(1997, 2, 28, 19, 30))]

    .. note:: Deprecated in 3.0. See SPARK-25496
    """
    warnings.warn("Deprecated in 3.0. See SPARK-25496", DeprecationWarning)
    sc = SparkContext._active_spark_context
    if isinstance(tz, Column):
        tz = _to_java_column(tz)
    return Column(sc._jvm.functions.from_utc_timestamp(_to_java_column(timestamp), tz))