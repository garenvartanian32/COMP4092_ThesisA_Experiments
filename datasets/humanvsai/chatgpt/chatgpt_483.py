import ctypes

def lookup_symbol(symbol_name):
    # try to lookup symbol locally
    try:
        return ctypes.pythonapi.PyObject_GetAttrString(ctypes.pythonapi.PyImport_ImportModule("__main__"), symbol_name)
    # if symbol is not local, look it up system wide
    except AttributeError:
        return ctypes.CDLL(None).lookup(symbol_name)
