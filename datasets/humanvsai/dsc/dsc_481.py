class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def asDictionary(self):
        return {
            'attribute1': self.attribute1,
            'attribute2': self.attribute2,
        }