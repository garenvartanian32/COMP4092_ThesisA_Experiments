def map_concat(*cols):
    """Returns the union of all the given maps.

    :param cols: list of column names (string) or list of :class:`Column` expressions

    >>> from pyspark.sql.functions import map_concat
    >>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as map1, map(3, 'c', 1, 'd') as map2")
    >>> df.select(map_concat("map1", "map2").alias("map3")).show(truncate=False)
    +------------------------+
    |map3                    |
    +------------------------+
    |[1 -> d, 2 -> b, 3 -> c]|
    +------------------------+
    """
    sc = SparkContext._active_spark_context
    if len(cols) == 1 and isinstance(cols[0], (list, set)):
        cols = cols[0]
    jc = sc._jvm.functions.map_concat(_to_seq(sc, cols, _to_java_column))
    return Column(jc)