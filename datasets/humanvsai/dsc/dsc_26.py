import inspect

def parameters(func):
    """Return a list where each element contains the parameters for a task."""
    sig = inspect.signature(func)
    return [name for name, _ in sig.parameters.items()]

def task(param1, param2, param3):
    pass

print(parameters(task))  # Output: ['param1', 'param2', 'param3']