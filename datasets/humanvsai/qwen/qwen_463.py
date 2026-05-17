def _listlike_guard(obj, name, iterable_only=False, log_warning=True):
    if isinstance(obj, str):
        if log_warning:
            print(f'Warning: {name} is a string. It will be treated as a single-element iterable.')
        return (obj,)
    elif isinstance(obj, collections.abc.Iterable):
        return obj
    else:
        raise TypeError(f'{name} must be an iterable, not {type(obj).__name__}')