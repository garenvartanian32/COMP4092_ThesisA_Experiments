def sequence(start, stop, step=None):
    """
    Generate a sequence of integers from `start` to `stop`, incrementing by `step`.
    If `step` is not set, incrementing by 1 if `start` is less than or equal to `stop`,
    otherwise -1.

    >>> df1 = spark.createDataFrame([(-2, 2)], ('C1', 'C2'))
    >>> df1.select(sequence('C1', 'C2').alias('r')).collect()
    [Row(r=[-2, -1, 0, 1, 2])]
    >>> df2 = spark.createDataFrame([(4, -4, -2)], ('C1', 'C2', 'C3'))
    >>> df2.select(sequence('C1', 'C2', 'C3').alias('r')).collect()
    [Row(r=[4, 2, 0, -2, -4])]
    """
    sc = SparkContext._active_spark_context
    if step is None:
        return Column(sc._jvm.functions.sequence(_to_java_column(start), _to_java_column(stop)))
    else:
        return Column(sc._jvm.functions.sequence(
            _to_java_column(start), _to_java_column(stop), _to_java_column(step)))