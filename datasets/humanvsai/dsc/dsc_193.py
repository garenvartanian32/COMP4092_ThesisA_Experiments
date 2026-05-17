def fullvars(obj):
    if hasattr(obj, '__dict__'):
        return vars(obj)
    elif hasattr(obj, '__slots__'):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        return {}