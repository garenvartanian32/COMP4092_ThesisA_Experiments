def private_method(func):

    def wrapper(self, *args, **kwargs):
        raise AttributeError(f"Private method '{func.__name__}' cannot be accessed.")
    return wrapper

def public_method(func):
    """Decorator for making an instance method public."""
    return func

class MyClass:

    @private_method
    def _private_method(self):
        print('This is a private method.')

    @public_method
    def public_method(self):
        print('This is a public method.')
obj = MyClass()