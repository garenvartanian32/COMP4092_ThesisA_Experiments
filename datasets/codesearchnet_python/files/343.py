def approx_count_distinct(col, rsd=None):
    """Aggregate function: returns a new :class:`Column` for approximate distinct count of
    column `col`.

    :param rsd: maximum estimation error allowed (default = 0.05). For rsd < 0.01, it is more
        efficient to use :func:`countDistinct`

    >>> df.agg(approx_count_distinct(df.age).alias('distinct_ages')).collect()
    [Row(distinct_ages=2)]
    """
    sc = SparkContext._active_spark_context
    if rsd is None:
        jc = sc._jvm.functions.approx_count_distinct(_to_java_column(col))
    else:
        jc = sc._jvm.functions.approx_count_distinct(_to_java_column(col), rsd)
    return Column(jc)