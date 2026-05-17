def array_position(col, value):
    """
    Collection function: Locates the position of the first occurrence of the given value
    in the given array. Returns null if either of the arguments are null.

    .. note:: The position is not zero based, but 1 based index. Returns 0 if the given
        value could not be found in the array.

    >>> df = spark.createDataFrame([(["c", "b", "a"],), ([],)], ['data'])
    >>> df.select(array_position(df.data, "a")).collect()
    [Row(array_position(data, a)=3), Row(array_position(data, a)=0)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.array_position(_to_java_column(col), value))