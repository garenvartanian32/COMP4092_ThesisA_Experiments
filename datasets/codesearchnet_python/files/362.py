def months_between(date1, date2, roundOff=True):
    """
    Returns number of months between dates date1 and date2.
    If date1 is later than date2, then the result is positive.
    If date1 and date2 are on the same day of month, or both are the last day of month,
    returns an integer (time of day will be ignored).
    The result is rounded off to 8 digits unless `roundOff` is set to `False`.

    >>> df = spark.createDataFrame([('1997-02-28 10:30:00', '1996-10-30')], ['date1', 'date2'])
    >>> df.select(months_between(df.date1, df.date2).alias('months')).collect()
    [Row(months=3.94959677)]
    >>> df.select(months_between(df.date1, df.date2, False).alias('months')).collect()
    [Row(months=3.9495967741935485)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.months_between(
        _to_java_column(date1), _to_java_column(date2), roundOff))