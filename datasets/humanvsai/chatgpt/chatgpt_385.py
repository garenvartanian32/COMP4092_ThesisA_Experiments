def rrr(cls):
    """Special class reloading function
    
    This function is often injected as rrr of classes.
    It reloads the class definition if it has been modified.
    """
    module = type(cls).__module__
    class_name = cls.__name__
    updated_class = getattr(importlib.import_module(module), class_name)
    if updated_class is not cls:
        cls.__dict__.update(updated_class.__dict__)
