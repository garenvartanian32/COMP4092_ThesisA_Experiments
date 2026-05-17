def element_at(col, extraction):
    """
    Collection function: Returns element of array at given index in extraction if col is array.
    Returns value for the given key in extraction if col is map.

    :param col: name of column containing array or map
    :param extraction: index to check for in array or key to check for in map

    .. note:: The position is not zero based, but 1 based index.

    >>> df = spark.createDataFrame([(["a", "b", "c"],), ([],)], ['data'])
    >>> df.select(element_at(df.data, 1)).collect()
    [Row(element_at(data, 1)=u'a'), Row(element_at(data, 1)=None)]

    >>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0},), ({},)], ['data'])
    >>> df.select(element_at(df.data, "a")).collect()
    [Row(element_at(data, a)=1.0), Row(element_at(data, a)=None)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.element_at(_to_java_column(col), extraction))