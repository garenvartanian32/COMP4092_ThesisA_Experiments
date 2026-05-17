class MyClass:
    def __init__(self):
        self._source = None

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value