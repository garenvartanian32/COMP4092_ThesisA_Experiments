class MyClass:
    def __init__(self):
        self.data = {}

    def set_value(self, key, value, confidence=100):
        """Defines the given value with the given confidence, unless the same
        value is already defined with a higher confidence level."""
        if key not in self.data or self.data[key][1] < confidence:
            self.data[key] = (value, confidence)