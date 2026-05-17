def process_input(input_obj):
    if isinstance(input_obj, str):
        return (input_obj,)
    elif hasattr(input_obj, '__iter__'):
        return input_obj
    else:
        raise TypeError("Object must be iterable")
