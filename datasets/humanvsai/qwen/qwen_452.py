def validator(self, meth):
    self._validators.append(meth)
    return meth

def validate(self):
    """Runs all validators.

        .. versionadded:: 17.1.0"""
    for validator in self._validators:
        validator(self)

class MyClass:

    def __init__(self):
        self._validators = []

    @validator
    def check_positive(self):
        """Check if a value is positive."""
        if self.value < 0:
            raise ValueError('Value must be positive')

    @validator
    def check_even(self):
        """Check if a value is even."""
        if self.value % 2 != 0:
            raise ValueError('Value must be even')

    def set_value(self, value):
        self.value = value
        self.validate()
obj = MyClass()