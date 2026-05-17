def copy(self):
        new = self.__class__()
        new.__dict__ = dict(self.__dict__)
        return new