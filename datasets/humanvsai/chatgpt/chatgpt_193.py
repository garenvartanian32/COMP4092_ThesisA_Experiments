def vars_with_slots(obj):
    return {key: getattr(obj, key) for key in vars(type(obj)).keys() if key not in ('__module__', '__dict__', '__weakref__')}

