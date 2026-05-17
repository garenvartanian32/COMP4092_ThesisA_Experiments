def persist(self, storageLevel):
        """
        Persists the underlying RDD with the specified storage level.
        """
        if not isinstance(storageLevel, StorageLevel):
            raise TypeError("`storageLevel` should be a StorageLevel, got %s" % type(storageLevel))
        javaStorageLevel = self._java_matrix_wrapper._sc._getJavaStorageLevel(storageLevel)
        self._java_matrix_wrapper.call("persist", javaStorageLevel)
        return self