def udf(f=None, returnType=StringType()):
    """Creates a user defined function (UDF).

    .. note:: The user-defined functions are considered deterministic by default. Due to
        optimization, duplicate invocations may be eliminated or the function may even be invoked
        more times than it is present in the query. If your function is not deterministic, call
        `asNondeterministic` on the user defined function. E.g.:

    >>> from pyspark.sql.types import IntegerType
    >>> import random
    >>> random_udf = udf(lambda: int(random.random() * 100), IntegerType()).asNondeterministic()

    .. note:: The user-defined functions do not support conditional expressions or short circuiting
        in boolean expressions and it ends up with being executed all internally. If the functions
        can fail on special rows, the workaround is to incorporate the condition into the functions.

    .. note:: The user-defined functions do not take keyword arguments on the calling side.

    :param f: python function if used as a standalone function
    :param returnType: the return type of the user-defined function. The value can be either a
        :class:`pyspark.sql.types.DataType` object or a DDL-formatted type string.

    >>> from pyspark.sql.types import IntegerType
    >>> slen = udf(lambda s: len(s), IntegerType())
    >>> @udf
    ... def to_upper(s):
    ...     if s is not None:
    ...         return s.upper()
    ...
    >>> @udf(returnType=IntegerType())
    ... def add_one(x):
    ...     if x is not None:
    ...         return x + 1
    ...
    >>> df = spark.createDataFrame([(1, "John Doe", 21)], ("id", "name", "age"))
    >>> df.select(slen("name").alias("slen(name)"), to_upper("name"), add_one("age")).show()
    +----------+--------------+------------+
    |slen(name)|to_upper(name)|add_one(age)|
    +----------+--------------+------------+
    |         8|      JOHN DOE|          22|
    +----------+--------------+------------+
    """

    # The following table shows most of Python data and SQL type conversions in normal UDFs that
    # are not yet visible to the user. Some of behaviors are buggy and might be changed in the near
    # future. The table might have to be eventually documented externally.
    # Please see SPARK-25666's PR to see the codes in order to generate the table below.
    #
    # +-----------------------------+--------------+----------+------+-------+---------------+---------------+--------------------+-----------------------------+----------+----------------------+---------+--------------------+-----------------+------------+--------------+------------------+----------------------+  # noqa
    # |SQL Type \ Python Value(Type)|None(NoneType)|True(bool)|1(int)|1(long)|         a(str)|     a(unicode)|    1970-01-01(date)|1970-01-01 00:00:00(datetime)|1.0(float)|array('i', [1])(array)|[1](list)|         (1,)(tuple)|   ABC(bytearray)|  1(Decimal)|{'a': 1}(dict)|Row(kwargs=1)(Row)|Row(namedtuple=1)(Row)|  # noqa
    # +-----------------------------+--------------+----------+------+-------+---------------+---------------+--------------------+-----------------------------+----------+----------------------+---------+--------------------+-----------------+------------+--------------+------------------+----------------------+  # noqa
    # |                      boolean|          None|      True|  None|   None|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                      tinyint|          None|      None|     1|      1|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                     smallint|          None|      None|     1|      1|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                          int|          None|      None|     1|      1|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                       bigint|          None|      None|     1|      1|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                       string|          None|   u'true'|  u'1'|   u'1'|           u'a'|           u'a'|u'java.util.Grego...|         u'java.util.Grego...|    u'1.0'|        u'[I@24a83055'|   u'[1]'|u'[Ljava.lang.Obj...|   u'[B@49093632'|        u'1'|      u'{a=1}'|                 X|                     X|  # noqa
    # |                         date|          None|         X|     X|      X|              X|              X|datetime.date(197...|         datetime.date(197...|         X|                     X|        X|                   X|                X|           X|             X|                 X|                     X|  # noqa
    # |                    timestamp|          None|         X|     X|      X|              X|              X|                   X|         datetime.datetime...|         X|                     X|        X|                   X|                X|           X|             X|                 X|                     X|  # noqa
    # |                        float|          None|      None|  None|   None|           None|           None|                None|                         None|       1.0|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                       double|          None|      None|  None|   None|           None|           None|                None|                         None|       1.0|                  None|     None|                None|             None|        None|          None|                 X|                     X|  # noqa
    # |                   array<int>|          None|      None|  None|   None|           None|           None|                None|                         None|      None|                   [1]|      [1]|                 [1]|     [65, 66, 67]|        None|          None|                 X|                     X|  # noqa
    # |                       binary|          None|      None|  None|   None|bytearray(b'a')|bytearray(b'a')|                None|                         None|      None|                  None|     None|                None|bytearray(b'ABC')|        None|          None|                 X|                     X|  # noqa
    # |                decimal(10,0)|          None|      None|  None|   None|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|Decimal('1')|          None|                 X|                     X|  # noqa
    # |              map<string,int>|          None|      None|  None|   None|           None|           None|                None|                         None|      None|                  None|     None|                None|             None|        None|     {u'a': 1}|                 X|                     X|  # noqa
    # |               struct<_1:int>|          None|         X|     X|      X|              X|              X|                   X|                            X|         X|                     X|Row(_1=1)|           Row(_1=1)|                X|           X|  Row(_1=None)|         Row(_1=1)|             Row(_1=1)|  # noqa
    # +-----------------------------+--------------+----------+------+-------+---------------+---------------+--------------------+-----------------------------+----------+----------------------+---------+--------------------+-----------------+------------+--------------+------------------+----------------------+  # noqa
    #
    # Note: DDL formatted string is used for 'SQL Type' for simplicity. This string can be
    #       used in `returnType`.
    # Note: The values inside of the table are generated by `repr`.
    # Note: Python 2 is used to generate this table since it is used to check the backward
    #       compatibility often in practice.
    # Note: 'X' means it throws an exception during the conversion.

    # decorator @udf, @udf(), @udf(dataType())
    if f is None or isinstance(f, (str, DataType)):
        # If DataType has been passed as a positional argument
        # for decorator use it as a returnType
        return_type = f or returnType
        return functools.partial(_create_udf, returnType=return_type,
                                 evalType=PythonEvalType.SQL_BATCHED_UDF)
    else:
        return _create_udf(f=f, returnType=returnType,
                           evalType=PythonEvalType.SQL_BATCHED_UDF)