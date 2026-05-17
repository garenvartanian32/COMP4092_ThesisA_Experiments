def setAll(self, pairs):
        """
        Set multiple parameters, passed as a list of key-value pairs.

        :param pairs: list of key-value pairs to set
        """
        for (k, v) in pairs:
            self.set(k, v)
        return self