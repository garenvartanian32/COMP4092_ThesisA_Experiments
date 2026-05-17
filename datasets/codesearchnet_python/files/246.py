def unpersist(self, blocking=False):
        """Marks the :class:`DataFrame` as non-persistent, and remove all blocks for it from
        memory and disk.

        .. note:: `blocking` default has changed to False to match Scala in 2.0.
        """
        self.is_cached = False
        self._jdf.unpersist(blocking)
        return self