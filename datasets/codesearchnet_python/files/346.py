def last(col, ignorenulls=False):
    """Aggregate function: returns the last value in a group.

    The function by default returns the last values it sees. It will return the last non-null
    value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

    .. note:: The function is non-deterministic because its results depends on order of rows
        which may be non-deterministic after a shuffle.
    """
    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.last(_to_java_column(col), ignorenulls)
    return Column(jc)