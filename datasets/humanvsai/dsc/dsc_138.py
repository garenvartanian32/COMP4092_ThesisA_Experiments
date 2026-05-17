class Colr:
    def __init__(self, value):
        self.value = value

    def strip(self, chars=None):
        if chars is None:
            self.value = self.value.strip()
        else:
            self.value = self.value.strip(chars)
        return self

# Usage
colr_instance = Colr("  Hello, World  ")
print(colr_instance.strip().value)  # "Hello, World"