def contains(self, key):
        """Does this configuration contain a given key?"""
        if self._jconf is not None:
            return self._jconf.contains(key)
        else:
            return key in self._conf