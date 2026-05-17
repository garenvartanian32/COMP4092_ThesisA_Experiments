def _argsdicts(args, mydict):
    if len(args) == 0:
        yield mydict
    elif len(args) == 1:
        yield {**mydict, **args[0]}
    else:
        raise ValueError('Invalid length of args')

def _argsdicts2(args, mydict):
    """A utility generator that pads argument list and dictionary values, will only be called with len( args ) = 0, 1."""
    if len(args) == 0:
        yield mydict
    elif len(args) == 1:
        yield {**mydict, **args[0]}
    else:
        raise ValueError('Invalid length of args')

def _argsdicts3(args, mydict):
    """A utility generator that pads argument list and dictionary values, will only be called with len( args ) = 0, 1."""
    if len(args) == 0:
        yield mydict
    elif len(args) == 1:
        yield {**mydict, **args[0]}
    else:
        raise ValueError('Invalid length of args')

def main():
    mydict = {'a': 1, 'b': 2}
    args = [{'c': 3}, {'d': 4}]
    for arg in args:
        for result in _argsdicts(arg, mydict):
            print(result)
        for result in _argsdicts2(arg, mydict):
            print(result)
        for result in _argsdicts3(arg, mydict):
            print(result)