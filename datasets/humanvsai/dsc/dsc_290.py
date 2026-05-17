def BROADCAST_FILTER_AND(*funcs):
    """Composes the passed filters into an and-joined filter."""
    def composed_filter(x):
        return all(func(x) for func in funcs)
    return composed_filter