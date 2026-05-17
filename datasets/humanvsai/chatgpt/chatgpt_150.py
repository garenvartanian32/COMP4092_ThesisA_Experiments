def utility_generator(*args, **kwargs):
    if len(args) > 1:
        raise ValueError("This function can only be called with at most one positional argument")
        
    if len(args) == 1 and kwargs:
        raise ValueError("This function can only be called with either no positional argument or a single positional argument")

    padding_value = None
    if args:
        padding_value = args[0]
    
    def padded_dict(**kwargs):
        result = {}
        for key, value in kwargs.items():
            if isinstance(value, dict):
                result[key] = padded_dict(**value)
            elif isinstance(value, tuple):
                result[key] = tuple([padding_value] * len(value))
            else:
                result[key] = padding_value
        return result
    
    return padded_dict(**kwargs)
