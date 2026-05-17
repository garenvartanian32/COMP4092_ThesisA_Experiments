class MyClass:
    def __init__(self):
        self.constants = [(0, "int", 10), (1, "str", "Hello"), (2, "float", 3.14)]

    def pretty_constants(self):
        return self.constants

# Usage
obj = MyClass()
print(obj.pretty_constants())