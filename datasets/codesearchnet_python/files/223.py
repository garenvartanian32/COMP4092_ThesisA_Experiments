def first_spark_call():
    """
    Return a CallSite representing the first Spark call in the current call stack.
    """
    tb = traceback.extract_stack()
    if len(tb) == 0:
        return None
    file, line, module, what = tb[len(tb) - 1]
    sparkpath = os.path.dirname(file)
    first_spark_frame = len(tb) - 1
    for i in range(0, len(tb)):
        file, line, fun, what = tb[i]
        if file.startswith(sparkpath):
            first_spark_frame = i
            break
    if first_spark_frame == 0:
        file, line, fun, what = tb[0]
        return CallSite(function=fun, file=file, linenum=line)
    sfile, sline, sfun, swhat = tb[first_spark_frame]
    ufile, uline, ufun, uwhat = tb[first_spark_frame - 1]
    return CallSite(function=sfun, file=ufile, linenum=uline)