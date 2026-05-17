def non_closure_comprehension(func, iterable):
    return [func(x) for x in iterable]
