class MyClass:
    def __init__(self):
        self._private_var = 10

    @private_method
    def _private_method(self):
        return self._private_var * 2

obj = MyClass()
print(obj._private_method())  # This will work

# But this will raise an AttributeError
print(obj._private_method)