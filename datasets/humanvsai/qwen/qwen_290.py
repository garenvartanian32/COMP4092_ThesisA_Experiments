def BROADCAST_FILTER_AND(*funcs):

    def filter_func(item):
        return all((f(item) for f in funcs))
    return filter_func

def BROADCAST_FILTER_OR(*funcs):
    """Composes the passed filters into an or-joined filter."""

    def filter_func(item):
        return any((f(item) for f in funcs))
    return filter_func

def BROADCAST_FILTER_NOT(func):
    """Composes the passed filter into a negated filter."""

    def filter_func(item):
        return not func(item)
    return filter_func

def BROADCAST_FILTER_XOR(*funcs):
    """Composes the passed filters into an xor-joined filter."""

    def filter_func(item):
        return sum((f(item) for f in funcs)) == 1
    return filter_func

def BROADCAST_FILTER_NAND(*funcs):
    """Composes the passed filters into a nand-joined filter."""

    def filter_func(item):
        return not all((f(item) for f in funcs))
    return filter_func

def BROADCAST_FILTER_NOR(*funcs):
    """Composes the passed filters into a nor-joined filter."""

    def filter_func(item):
        return not any((f(item) for f in funcs))
    return filter_func

def BROADCAST_FILTER_XNOR(*funcs):
    """Composes the passed filters into an xnor-joined filter."""

    def filter_func(item):
        return sum((f(item) for f in funcs)) % 2 == 0
    return filter_func

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0
and_filter = BROADCAST_FILTER_AND(is_even, is_positive)
or_filter = BROADCAST_FILTER_OR(is_even, is_positive)
not_filter = BROADCAST_FILTER_NOT(is_even)
xor_filter = BROADCAST_FILTER_XOR(is_even, is_positive)
nand_filter = BROADCAST_FILTER_NAND(is_even, is_positive)
nor_filter = BROADCAST_FILTER_NOR(is_even, is_positive)
xnor_filter = BROADCAST_FILTER_XNOR(is_even, is_positive)
test_values = [-2, -1, 0, 1, 2]