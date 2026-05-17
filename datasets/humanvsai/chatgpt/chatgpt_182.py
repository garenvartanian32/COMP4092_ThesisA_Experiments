def resolve_attributes(obj, kwargs):
    for key in kwargs:
        if isinstance(kwargs[key], str) and kwargs[key].startswith("<") and kwargs[key].endswith(">"):
            attribute_name = kwargs[key][1:-1]
            if hasattr(obj, attribute_name):
                kwargs[key] = getattr(obj, attribute_name)
    return kwargs
