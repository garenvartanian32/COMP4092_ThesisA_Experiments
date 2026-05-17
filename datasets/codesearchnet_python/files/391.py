def array_remove(col, element):
    """
    Collection function: Remove all elements that equal to element from the given array.

    :param col: name of column containing array
    :param element: element to be removed from the array

    >>> df = spark.createDataFrame([([1, 2, 3, 1, 1],), ([],)], ['data'])
    >>> df.select(array_remove(df.data, 1)).collect()
    [Row(array_remove(data, 1)=[2, 3]), Row(array_remove(data, 1)=[])]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.array_remove(_to_java_column(col), element))