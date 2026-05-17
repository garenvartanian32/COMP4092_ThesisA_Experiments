def _function_lookup(name, module):
    try:
        return getattr(module, name)
    except AttributeError:
        importlib.import_module(module.__name__)
        return getattr(module, name)

def register_function(name, function):
    """Registers a function with a given name."""
    globals()[name] = function

def get_function(name):
    """Retrieves a function by its name."""
    return globals()[name]