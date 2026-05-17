def schema_of_json(json, options={}):
    """
    Parses a JSON string and infers its schema in DDL format.

    :param json: a JSON string or a string literal containing a JSON string.
    :param options: options to control parsing. accepts the same options as the JSON datasource

    .. versionchanged:: 3.0
       It accepts `options` parameter to control schema inferring.

    >>> df = spark.range(1)
    >>> df.select(schema_of_json(lit('{"a": 0}')).alias("json")).collect()
    [Row(json=u'struct<a:bigint>')]
    >>> schema = schema_of_json('{a: 1}', {'allowUnquotedFieldNames':'true'})
    >>> df.select(schema.alias("json")).collect()
    [Row(json=u'struct<a:bigint>')]
    """
    if isinstance(json, basestring):
        col = _create_column_from_literal(json)
    elif isinstance(json, Column):
        col = _to_java_column(json)
    else:
        raise TypeError("schema argument should be a column or string")

    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.schema_of_json(col, options)
    return Column(jc)