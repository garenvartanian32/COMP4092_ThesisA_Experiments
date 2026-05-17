import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def copy(self):
        return copy.copy(self)

# Create an instance of MyClass
obj1 = MyClass(10)

# Create a shallow copy of obj1
obj2 = obj1.copy()

print(obj1)  # Output: 10
print(obj2)  # Output: 10