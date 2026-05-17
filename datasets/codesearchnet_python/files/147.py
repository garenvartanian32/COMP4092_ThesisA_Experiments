def set(self, key, value):
        """Set a configuration property."""
        # Try to set self._jconf first if JVM is created, set self._conf if JVM is not created yet.
        if self._jconf is not None:
            self._jconf.set(key, unicode(value))
        else:
            self._conf[key] = unicode(value)
        return self