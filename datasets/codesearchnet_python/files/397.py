def to_csv(col, options={}):
    """
    Converts a column containing a :class:`StructType` into a CSV string.
    Throws an exception, in the case of an unsupported type.

    :param col: name of column containing a struct.
    :param options: options to control converting. accepts the same options as the CSV datasource.

    >>> from pyspark.sql import Row
    >>> data = [(1, Row(name='Alice', age=2))]
    >>> df = spark.createDataFrame(data, ("key", "value"))
    >>> df.select(to_csv(df.value).alias("csv")).collect()
    [Row(csv=u'2,Alice')]
    """

    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.to_csv(_to_java_column(col), options)
    return Column(jc)