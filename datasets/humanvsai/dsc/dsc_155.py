class MyClass:
    def __init__(self):
        self.views = []

    def populate(self):
        """Populate this list with all views that take no arguments."""
        for name, method in inspect.getmembers(self, inspect.ismethod):
            if not method.__code__.co_argcount:
                self.views.append(method)