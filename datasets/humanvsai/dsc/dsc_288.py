class MyClass:
    def __init__(self, name=None):
        self.name = name

    def _project_name(self):
        if self.name is None:
            raise ValueError("There is no name")
        return self.name