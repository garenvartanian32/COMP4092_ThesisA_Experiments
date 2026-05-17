def persist(self, storageLevel):
        """
        Persist the RDDs of this DStream with the given storage level
        """
        self.is_cached = True
        javaStorageLevel = self._sc._getJavaStorageLevel(storageLevel)
        self._jdstream.persist(javaStorageLevel)
        return self