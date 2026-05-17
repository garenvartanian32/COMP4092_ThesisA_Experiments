def is_supported(self, target):
    return target in self.definitions

class MyClass:

    def __init__(self, definitions):
        self.definitions = definitions

    def is_supported(self, target):
        """Returns True if target is supported by definitions"""
        return target in self.definitions
my_instance = MyClass(['a', 'b', 'c'])