def _create_function_over_column(name, doc=""):
    """Similar with `_create_function` but creates a PySpark function that takes a column
    (as string as well). This is mainly for PySpark functions to take strings as
    column names.
    """
    def _(col):
        sc = SparkContext._active_spark_context
        jc = getattr(sc._jvm.functions, name)(_to_java_column(col))
        return Column(jc)
    _.__name__ = name
    _.__doc__ = doc
    return _