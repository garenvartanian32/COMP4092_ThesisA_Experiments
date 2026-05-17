def storageLevel(self):
        """Get the :class:`DataFrame`'s current storage level.

        >>> df.storageLevel
        StorageLevel(False, False, False, False, 1)
        >>> df.cache().storageLevel
        StorageLevel(True, True, False, True, 1)
        >>> df2.persist(StorageLevel.DISK_ONLY_2).storageLevel
        StorageLevel(True, False, False, False, 2)
        """
        java_storage_level = self._jdf.storageLevel()
        storage_level = StorageLevel(java_storage_level.useDisk(),
                                     java_storage_level.useMemory(),
                                     java_storage_level.useOffHeap(),
                                     java_storage_level.deserialized(),
                                     java_storage_level.replication())
        return storage_level