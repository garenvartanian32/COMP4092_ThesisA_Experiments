def convert_yielded(yielded):
    # Lists and dicts containing YieldPoints were handled earlier.
    if yielded is None:
        return moment
    elif isinstance(yielded, (list, dict)):
        return multi(yielded)
    elif is_future(yielded):
        return yielded
    elif isawaitable(yielded):
        return _wrap_awaitable(yielded)
    else:
        raise BadYieldError("yielded unknown object %r" % (yielded,))