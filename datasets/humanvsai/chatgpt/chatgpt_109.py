import builtins

def is_builtin(name):
    return name in dir(builtins)
