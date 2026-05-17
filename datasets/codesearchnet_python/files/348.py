def rand(seed=None):
    """Generates a random column with independent and identically distributed (i.i.d.) samples
    from U[0.0, 1.0].

    .. note:: The function is non-deterministic in general case.

    >>> df.withColumn('rand', rand(seed=42) * 3).collect()
    [Row(age=2, name=u'Alice', rand=2.4052597283576684),
     Row(age=5, name=u'Bob', rand=2.3913904055683974)]
    """
    sc = SparkContext._active_spark_context
    if seed is not None:
        jc = sc._jvm.functions.rand(seed)
    else:
        jc = sc._jvm.functions.rand()
    return Column(jc)