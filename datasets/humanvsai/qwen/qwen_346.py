def getEntropies(m):
    currentEntropy = 0
    maxEntropy = 0
    for attr in dir(m):
        if attr.startswith('__'):
            continue
        try:
            obj = getattr(m, attr)
            if isinstance(obj, types.ModuleType):
                (childCurrentEntropy, childMaxEntropy) = getEntropies(obj)
                currentEntropy += childCurrentEntropy
                maxEntropy += childMaxEntropy
            elif isinstance(obj, types.FunctionType):
                currentEntropy += calculateEntropy(obj)
                maxEntropy += calculateMaxEntropy(obj)
        except AttributeError:
            continue
    return (currentEntropy, maxEntropy)

def calculateEntropy(f):
    """Calculate the entropy of a function

  :param f: a function

  :return: entropy value"""
    return 0

def calculateMaxEntropy(f):
    """Calculate the maximum possible entropy of a function

  :param f: a function

  :return: max entropy value"""
    return 0