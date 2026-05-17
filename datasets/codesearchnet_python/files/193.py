def filter(self, f):
        """
        Return a new DStream containing only the elements that satisfy predicate.
        """
        def func(iterator):
            return filter(f, iterator)
        return self.mapPartitions(func, True)