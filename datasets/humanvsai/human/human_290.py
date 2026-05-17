def BROADCAST_FILTER_AND(*funcs):
        return lambda u, command, *args, **kwargs: all(f(u, command, *args, **kwargs) for f in funcs)