def filtered(self, indices):
        if indices is None or len(indices) == len(self):
            return self
        new = object.__new__(self.__class__)
        indices = numpy.uint32(sorted(indices))
        new.array = self.array[indices]
        new.complete = self.complete
        return new