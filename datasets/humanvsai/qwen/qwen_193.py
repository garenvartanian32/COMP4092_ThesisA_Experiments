def fullvars(obj):
    if hasattr(obj, '__slots__'):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        return vars(obj)

def fullvars_with_class(obj):
    """like `fullvars()` but also include class attributes."""
    class_vars = {k: v for (k, v) in obj.__class__.__dict__.items() if not k.startswith('__')}
    instance_vars = fullvars(obj)
    return {**class_vars, **instance_vars}

class MyClass:
    class_attr = 42

    def __init__(self, value):
        self.instance_attr = value
obj = MyClass(10)