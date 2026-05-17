def _listlike_guard(obj, name, iterable_only=False, log_warning=True):
    """We frequently require passed objects to support iteration or
    containment expressions, but not be strings. (Of course, strings
    support iteration and containment, but not usefully.)  If the passed
    object is a string, we'll wrap it in a tuple and return it. If it's
    already an iterable, we'll return it as-is. Otherwise, we'll raise a
    TypeError."""

    if isinstance(obj, str):
        return (obj,)
    elif iterable_only and not isinstance(obj, collections.abc.Iterable):
        raise TypeError(f"{name} must be an iterable")
    elif not iterable_only and not isinstance(obj, (collections.abc.Iterable, str)):
        raise TypeError(f"{name} must be an iterable or a string")
    else:
        return obj