class MyClass:
    def __init__(self):
        self.index = []

    def countIndex(self):
        """A wrapper for the count function in calcrepo.index; count using specified parameters"""
        return self.index.count()