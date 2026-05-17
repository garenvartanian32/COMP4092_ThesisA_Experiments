def map(self, f, preservesPartitioning=False):
        """
        Return a new DStream by applying a function to each element of DStream.
        """
        def func(iterator):
            return map(f, iterator)
        return self.mapPartitions(func, preservesPartitioning)