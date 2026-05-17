def pandas_udf(f=None, returnType=None, functionType=None):
    """
    Creates a vectorized user defined function (UDF).

    :param f: user-defined function. A python function if used as a standalone function
    :param returnType: the return type of the user-defined function. The value can be either a
        :class:`pyspark.sql.types.DataType` object or a DDL-formatted type string.
    :param functionType: an enum value in :class:`pyspark.sql.functions.PandasUDFType`.
                         Default: SCALAR.

    .. note:: Experimental

    The function type of the UDF can be one of the following:

    1. SCALAR

       A scalar UDF defines a transformation: One or more `pandas.Series` -> A `pandas.Series`.
       The length of the returned `pandas.Series` must be of the same as the input `pandas.Series`.
       If the return type is :class:`StructType`, the returned value should be a `pandas.DataFrame`.

       :class:`MapType`, nested :class:`StructType` are currently not supported as output types.

       Scalar UDFs are used with :meth:`pyspark.sql.DataFrame.withColumn` and
       :meth:`pyspark.sql.DataFrame.select`.

       >>> from pyspark.sql.functions import pandas_udf, PandasUDFType
       >>> from pyspark.sql.types import IntegerType, StringType
       >>> slen = pandas_udf(lambda s: s.str.len(), IntegerType())  # doctest: +SKIP
       >>> @pandas_udf(StringType())  # doctest: +SKIP
       ... def to_upper(s):
       ...     return s.str.upper()
       ...
       >>> @pandas_udf("integer", PandasUDFType.SCALAR)  # doctest: +SKIP
       ... def add_one(x):
       ...     return x + 1
       ...
       >>> df = spark.createDataFrame([(1, "John Doe", 21)],
       ...                            ("id", "name", "age"))  # doctest: +SKIP
       >>> df.select(slen("name").alias("slen(name)"), to_upper("name"), add_one("age")) \\
       ...     .show()  # doctest: +SKIP
       +----------+--------------+------------+
       |slen(name)|to_upper(name)|add_one(age)|
       +----------+--------------+------------+
       |         8|      JOHN DOE|          22|
       +----------+--------------+------------+
       >>> @pandas_udf("first string, last string")  # doctest: +SKIP
       ... def split_expand(n):
       ...     return n.str.split(expand=True)
       >>> df.select(split_expand("name")).show()  # doctest: +SKIP
       +------------------+
       |split_expand(name)|
       +------------------+
       |       [John, Doe]|
       +------------------+

       .. note:: The length of `pandas.Series` within a scalar UDF is not that of the whole input
           column, but is the length of an internal batch used for each call to the function.
           Therefore, this can be used, for example, to ensure the length of each returned
           `pandas.Series`, and can not be used as the column length.

    2. GROUPED_MAP

       A grouped map UDF defines transformation: A `pandas.DataFrame` -> A `pandas.DataFrame`
       The returnType should be a :class:`StructType` describing the schema of the returned
       `pandas.DataFrame`. The column labels of the returned `pandas.DataFrame` must either match
       the field names in the defined returnType schema if specified as strings, or match the
       field data types by position if not strings, e.g. integer indices.
       The length of the returned `pandas.DataFrame` can be arbitrary.

       Grouped map UDFs are used with :meth:`pyspark.sql.GroupedData.apply`.

       >>> from pyspark.sql.functions import pandas_udf, PandasUDFType
       >>> df = spark.createDataFrame(
       ...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
       ...     ("id", "v"))  # doctest: +SKIP
       >>> @pandas_udf("id long, v double", PandasUDFType.GROUPED_MAP)  # doctest: +SKIP
       ... def normalize(pdf):
       ...     v = pdf.v
       ...     return pdf.assign(v=(v - v.mean()) / v.std())
       >>> df.groupby("id").apply(normalize).show()  # doctest: +SKIP
       +---+-------------------+
       | id|                  v|
       +---+-------------------+
       |  1|-0.7071067811865475|
       |  1| 0.7071067811865475|
       |  2|-0.8320502943378437|
       |  2|-0.2773500981126146|
       |  2| 1.1094003924504583|
       +---+-------------------+

       Alternatively, the user can define a function that takes two arguments.
       In this case, the grouping key(s) will be passed as the first argument and the data will
       be passed as the second argument. The grouping key(s) will be passed as a tuple of numpy
       data types, e.g., `numpy.int32` and `numpy.float64`. The data will still be passed in
       as a `pandas.DataFrame` containing all columns from the original Spark DataFrame.
       This is useful when the user does not want to hardcode grouping key(s) in the function.

       >>> import pandas as pd  # doctest: +SKIP
       >>> from pyspark.sql.functions import pandas_udf, PandasUDFType
       >>> df = spark.createDataFrame(
       ...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
       ...     ("id", "v"))  # doctest: +SKIP
       >>> @pandas_udf("id long, v double", PandasUDFType.GROUPED_MAP)  # doctest: +SKIP
       ... def mean_udf(key, pdf):
       ...     # key is a tuple of one numpy.int64, which is the value
       ...     # of 'id' for the current group
       ...     return pd.DataFrame([key + (pdf.v.mean(),)])
       >>> df.groupby('id').apply(mean_udf).show()  # doctest: +SKIP
       +---+---+
       | id|  v|
       +---+---+
       |  1|1.5|
       |  2|6.0|
       +---+---+
       >>> @pandas_udf(
       ...    "id long, `ceil(v / 2)` long, v double",
       ...    PandasUDFType.GROUPED_MAP)  # doctest: +SKIP
       >>> def sum_udf(key, pdf):
       ...     # key is a tuple of two numpy.int64s, which is the values
       ...     # of 'id' and 'ceil(df.v / 2)' for the current group
       ...     return pd.DataFrame([key + (pdf.v.sum(),)])
       >>> df.groupby(df.id, ceil(df.v / 2)).apply(sum_udf).show()  # doctest: +SKIP
       +---+-----------+----+
       | id|ceil(v / 2)|   v|
       +---+-----------+----+
       |  2|          5|10.0|
       |  1|          1| 3.0|
       |  2|          3| 5.0|
       |  2|          2| 3.0|
       +---+-----------+----+

       .. note:: If returning a new `pandas.DataFrame` constructed with a dictionary, it is
           recommended to explicitly index the columns by name to ensure the positions are correct,
           or alternatively use an `OrderedDict`.
           For example, `pd.DataFrame({'id': ids, 'a': data}, columns=['id', 'a'])` or
           `pd.DataFrame(OrderedDict([('id', ids), ('a', data)]))`.

       .. seealso:: :meth:`pyspark.sql.GroupedData.apply`

    3. GROUPED_AGG

       A grouped aggregate UDF defines a transformation: One or more `pandas.Series` -> A scalar
       The `returnType` should be a primitive data type, e.g., :class:`DoubleType`.
       The returned scalar can be either a python primitive type, e.g., `int` or `float`
       or a numpy data type, e.g., `numpy.int64` or `numpy.float64`.

       :class:`MapType` and :class:`StructType` are currently not supported as output types.

       Group aggregate UDFs are used with :meth:`pyspark.sql.GroupedData.agg` and
       :class:`pyspark.sql.Window`

       This example shows using grouped aggregated UDFs with groupby:

       >>> from pyspark.sql.functions import pandas_udf, PandasUDFType
       >>> df = spark.createDataFrame(
       ...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
       ...     ("id", "v"))
       >>> @pandas_udf("double", PandasUDFType.GROUPED_AGG)  # doctest: +SKIP
       ... def mean_udf(v):
       ...     return v.mean()
       >>> df.groupby("id").agg(mean_udf(df['v'])).show()  # doctest: +SKIP
       +---+-----------+
       | id|mean_udf(v)|
       +---+-----------+
       |  1|        1.5|
       |  2|        6.0|
       +---+-----------+

       This example shows using grouped aggregated UDFs as window functions.

       >>> from pyspark.sql.functions import pandas_udf, PandasUDFType
       >>> from pyspark.sql import Window
       >>> df = spark.createDataFrame(
       ...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
       ...     ("id", "v"))
       >>> @pandas_udf("double", PandasUDFType.GROUPED_AGG)  # doctest: +SKIP
       ... def mean_udf(v):
       ...     return v.mean()
       >>> w = (Window.partitionBy('id')
       ...            .orderBy('v')
       ...            .rowsBetween(-1, 0))
       >>> df.withColumn('mean_v', mean_udf(df['v']).over(w)).show()  # doctest: +SKIP
       +---+----+------+
       | id|   v|mean_v|
       +---+----+------+
       |  1| 1.0|   1.0|
       |  1| 2.0|   1.5|
       |  2| 3.0|   3.0|
       |  2| 5.0|   4.0|
       |  2|10.0|   7.5|
       +---+----+------+

       .. note:: For performance reasons, the input series to window functions are not copied.
            Therefore, mutating the input series is not allowed and will cause incorrect results.
            For the same reason, users should also not rely on the index of the input series.

       .. seealso:: :meth:`pyspark.sql.GroupedData.agg` and :class:`pyspark.sql.Window`

    .. note:: The user-defined functions are considered deterministic by default. Due to
        optimization, duplicate invocations may be eliminated or the function may even be invoked
        more times than it is present in the query. If your function is not deterministic, call
        `asNondeterministic` on the user defined function. E.g.:

    >>> @pandas_udf('double', PandasUDFType.SCALAR)  # doctest: +SKIP
    ... def random(v):
    ...     import numpy as np
    ...     import pandas as pd
    ...     return pd.Series(np.random.randn(len(v))
    >>> random = random.asNondeterministic()  # doctest: +SKIP

    .. note:: The user-defined functions do not support conditional expressions or short circuiting
        in boolean expressions and it ends up with being executed all internally. If the functions
        can fail on special rows, the workaround is to incorporate the condition into the functions.

    .. note:: The user-defined functions do not take keyword arguments on the calling side.

    .. note:: The data type of returned `pandas.Series` from the user-defined functions should be
        matched with defined returnType (see :meth:`types.to_arrow_type` and
        :meth:`types.from_arrow_type`). When there is mismatch between them, Spark might do
        conversion on returned data. The conversion is not guaranteed to be correct and results
        should be checked for accuracy by users.
    """

    # The following table shows most of Pandas data and SQL type conversions in Pandas UDFs that
    # are not yet visible to the user. Some of behaviors are buggy and might be changed in the near
    # future. The table might have to be eventually documented externally.
    # Please see SPARK-25798's PR to see the codes in order to generate the table below.
    #
    # +-----------------------------+----------------------+----------+-------+--------+--------------------+--------------------+--------+---------+---------+---------+------------+------------+------------+-----------------------------------+-----------------------------------------------------+-----------------+--------------------+-----------------------------+-------------+-----------------+------------------+-----------+--------------------------------+  # noqa
    # |SQL Type \ Pandas Value(Type)|None(object(NoneType))|True(bool)|1(int8)|1(int16)|            1(int32)|            1(int64)|1(uint8)|1(uint16)|1(uint32)|1(uint64)|1.0(float16)|1.0(float32)|1.0(float64)|1970-01-01 00:00:00(datetime64[ns])|1970-01-01 00:00:00-05:00(datetime64[ns, US/Eastern])|a(object(string))|  1(object(Decimal))|[1 2 3](object(array[int32]))|1.0(float128)|(1+0j)(complex64)|(1+0j)(complex128)|A(category)|1 days 00:00:00(timedelta64[ns])|  # noqa
    # +-----------------------------+----------------------+----------+-------+--------+--------------------+--------------------+--------+---------+---------+---------+------------+------------+------------+-----------------------------------+-----------------------------------------------------+-----------------+--------------------+-----------------------------+-------------+-----------------+------------------+-----------+--------------------------------+  # noqa
    # |                      boolean|                  None|      True|   True|    True|                True|                True|    True|     True|     True|     True|       False|       False|       False|                              False|                                                False|                X|                   X|                            X|        False|            False|             False|          X|                           False|  # noqa
    # |                      tinyint|                  None|         1|      1|       1|                   1|                   1|       X|        X|        X|        X|           1|           1|           1|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          0|                               X|  # noqa
    # |                     smallint|                  None|         1|      1|       1|                   1|                   1|       1|        X|        X|        X|           1|           1|           1|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                          int|                  None|         1|      1|       1|                   1|                   1|       1|        1|        X|        X|           1|           1|           1|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                       bigint|                  None|         1|      1|       1|                   1|                   1|       1|        1|        1|        X|           1|           1|           1|                                  0|                                       18000000000000|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                        float|                  None|       1.0|    1.0|     1.0|                 1.0|                 1.0|     1.0|      1.0|      1.0|      1.0|         1.0|         1.0|         1.0|                                  X|                                                    X|                X|1.401298464324817...|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                       double|                  None|       1.0|    1.0|     1.0|                 1.0|                 1.0|     1.0|      1.0|      1.0|      1.0|         1.0|         1.0|         1.0|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                         date|                  None|         X|      X|       X|datetime.date(197...|                   X|       X|        X|        X|        X|           X|           X|           X|               datetime.date(197...|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                    timestamp|                  None|         X|      X|       X|                   X|datetime.datetime...|       X|        X|        X|        X|           X|           X|           X|               datetime.datetime...|                                 datetime.datetime...|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                       string|                  None|       u''|u'\x01'| u'\x01'|             u'\x01'|             u'\x01'| u'\x01'|  u'\x01'|  u'\x01'|  u'\x01'|         u''|         u''|         u''|                                  X|                                                    X|             u'a'|                   X|                            X|          u''|              u''|               u''|          X|                               X|  # noqa
    # |                decimal(10,0)|                  None|         X|      X|       X|                   X|                   X|       X|        X|        X|        X|           X|           X|           X|                                  X|                                                    X|                X|        Decimal('1')|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                   array<int>|                  None|         X|      X|       X|                   X|                   X|       X|        X|        X|        X|           X|           X|           X|                                  X|                                                    X|                X|                   X|                    [1, 2, 3]|            X|                X|                 X|          X|                               X|  # noqa
    # |              map<string,int>|                     X|         X|      X|       X|                   X|                   X|       X|        X|        X|        X|           X|           X|           X|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |               struct<_1:int>|                     X|         X|      X|       X|                   X|                   X|       X|        X|        X|        X|           X|           X|           X|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # |                       binary|                     X|         X|      X|       X|                   X|                   X|       X|        X|        X|        X|           X|           X|           X|                                  X|                                                    X|                X|                   X|                            X|            X|                X|                 X|          X|                               X|  # noqa
    # +-----------------------------+----------------------+----------+-------+--------+--------------------+--------------------+--------+---------+---------+---------+------------+------------+------------+-----------------------------------+-----------------------------------------------------+-----------------+--------------------+-----------------------------+-------------+-----------------+------------------+-----------+--------------------------------+  # noqa
    #
    # Note: DDL formatted string is used for 'SQL Type' for simplicity. This string can be
    #       used in `returnType`.
    # Note: The values inside of the table are generated by `repr`.
    # Note: Python 2 is used to generate this table since it is used to check the backward
    #       compatibility often in practice.
    # Note: Pandas 0.19.2 and PyArrow 0.9.0 are used.
    # Note: Timezone is Singapore timezone.
    # Note: 'X' means it throws an exception during the conversion.
    # Note: 'binary' type is only supported with PyArrow 0.10.0+ (SPARK-23555).

    # decorator @pandas_udf(returnType, functionType)
    is_decorator = f is None or isinstance(f, (str, DataType))

    if is_decorator:
        # If DataType has been passed as a positional argument
        # for decorator use it as a returnType
        return_type = f or returnType

        if functionType is not None:
            # @pandas_udf(dataType, functionType=functionType)
            # @pandas_udf(returnType=dataType, functionType=functionType)
            eval_type = functionType
        elif returnType is not None and isinstance(returnType, int):
            # @pandas_udf(dataType, functionType)
            eval_type = returnType
        else:
            # @pandas_udf(dataType) or @pandas_udf(returnType=dataType)
            eval_type = PythonEvalType.SQL_SCALAR_PANDAS_UDF
    else:
        return_type = returnType

        if functionType is not None:
            eval_type = functionType
        else:
            eval_type = PythonEvalType.SQL_SCALAR_PANDAS_UDF

    if return_type is None:
        raise ValueError("Invalid returnType: returnType can not be None")

    if eval_type not in [PythonEvalType.SQL_SCALAR_PANDAS_UDF,
                         PythonEvalType.SQL_GROUPED_MAP_PANDAS_UDF,
                         PythonEvalType.SQL_GROUPED_AGG_PANDAS_UDF]:
        raise ValueError("Invalid functionType: "
                         "functionType must be one the values from PandasUDFType")

    if is_decorator:
        return functools.partial(_create_udf, returnType=return_type, evalType=eval_type)
    else:
        return _create_udf(f=f, returnType=return_type, evalType=eval_type)