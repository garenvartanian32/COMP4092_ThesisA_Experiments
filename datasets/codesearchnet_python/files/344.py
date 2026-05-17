def broadcast(df):
    """Marks a DataFrame as small enough for use in broadcast joins."""

    sc = SparkContext._active_spark_context
    return DataFrame(sc._jvm.functions.broadcast(df._jdf), df.sql_ctx)