def persist(self, storageLevel=StorageLevel.MEMORY_AND_DISK):
        """Sets the storage level to persist the contents of the :class:`DataFrame` across
        operations after the first time it is computed. This can only be used to assign
        a new storage level if the :class:`DataFrame` does not have a storage level set yet.
        If no storage level is specified defaults to (C{MEMORY_AND_DISK}).

        .. note:: The default storage level has changed to C{MEMORY_AND_DISK} to match Scala in 2.0.
        """
        self.is_cached = True
        javaStorageLevel = self._sc._getJavaStorageLevel(storageLevel)
        self._jdf.persist(javaStorageLevel)
        return self