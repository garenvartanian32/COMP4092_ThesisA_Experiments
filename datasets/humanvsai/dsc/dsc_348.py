def _function_lookup(name, module):
    """Searches the function between the registered ones.
    If not found, it imports the module forcing its registration."""
    # Check if the function exists in the module
    if hasattr(module, name):
        return getattr(module, name)
    else:
        # If not found, import the module to force its registration
        exec(f"import {module}")
        if hasattr(module, name):
            return getattr(module, name)
        else:
            raise ImportError(f"Function {name} not found in module {module}")