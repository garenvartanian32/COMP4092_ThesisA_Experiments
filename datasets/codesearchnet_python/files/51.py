def cache(self):
        """
        Persist this RDD with the default storage level (C{MEMORY_ONLY}).
        """
        self.is_cached = True
        self.persist(StorageLevel.MEMORY_ONLY)
        return self