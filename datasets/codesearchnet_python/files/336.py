def get(self, key, default=_NoValue):
        """Returns the value of Spark runtime configuration property for the given key,
        assuming it is set.
        """
        self._checkType(key, "key")
        if default is _NoValue:
            return self._jconf.get(key)
        else:
            if default is not None:
                self._checkType(default, "default")
            return self._jconf.get(key, default)