def private(method):
    def inner(self, *args, **kwargs):
        if not self.__class__.__name__.startswith("_"):
            raise ValueError("Method {} is private and cannot be accessed from outside the class".format(method.__name__))
        else:
            return method(self, *args, **kwargs)
    return inner
