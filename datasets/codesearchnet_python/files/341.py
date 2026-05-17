def _create_binary_mathfunction(name, doc=""):
    """ Create a binary mathfunction by name"""
    def _(col1, col2):
        sc = SparkContext._active_spark_context
        # For legacy reasons, the arguments here can be implicitly converted into floats,
        # if they are not columns or strings.
        if isinstance(col1, Column):
            arg1 = col1._jc
        elif isinstance(col1, basestring):
            arg1 = _create_column_from_name(col1)
        else:
            arg1 = float(col1)

        if isinstance(col2, Column):
            arg2 = col2._jc
        elif isinstance(col2, basestring):
            arg2 = _create_column_from_name(col2)
        else:
            arg2 = float(col2)

        jc = getattr(sc._jvm.functions, name)(arg1, arg2)
        return Column(jc)
    _.__name__ = name
    _.__doc__ = doc
    return _