def callMLlibFunc(name, *args):
    """ Call API in PythonMLLibAPI """
    sc = SparkContext.getOrCreate()
    api = getattr(sc._jvm.PythonMLLibAPI(), name)
    return callJavaFunc(sc, api, *args)