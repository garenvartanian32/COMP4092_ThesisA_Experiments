def fullvars(obj):
    try:
        return vars(obj)
    except TypeError:
        pass
    # __slots__
    slotsnames = set()
    for cls in type(obj).__mro__:
        __slots__ = getattr(cls, '__slots__', None)
        if __slots__:
            if isinstance(__slots__, str):
                slotsnames.add(__slots__)
            else:
                slotsnames.update(__slots__)
    return _SlotsProxy(obj, slotsnames)