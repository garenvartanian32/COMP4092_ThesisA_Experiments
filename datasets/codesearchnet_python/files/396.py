def schema_of_csv(csv, options={}):
    """
    Parses a CSV string and infers its schema in DDL format.

    :param col: a CSV string or a string literal containing a CSV string.
    :param options: options to control parsing. accepts the same options as the CSV datasource

    >>> df = spark.range(1)
    >>> df.select(schema_of_csv(lit('1|a'), {'sep':'|'}).alias("csv")).collect()
    [Row(csv=u'struct<_c0:int,_c1:string>')]
    >>> df.select(schema_of_csv('1|a', {'sep':'|'}).alias("csv")).collect()
    [Row(csv=u'struct<_c0:int,_c1:string>')]
    """
    if isinstance(csv, basestring):
        col = _create_column_from_literal(csv)
    elif isinstance(csv, Column):
        col = _to_java_column(csv)
    else:
        raise TypeError("schema argument should be a column or string")

    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.schema_of_csv(col, options)
    return Column(jc)