def unpersist(self, blocking=False):
        """
        Mark the RDD as non-persistent, and remove all blocks for it from
        memory and disk.

        .. versionchanged:: 3.0.0
           Added optional argument `blocking` to specify whether to block until all
           blocks are deleted.
        """
        self.is_cached = False
        self._jrdd.unpersist(blocking)
        return self