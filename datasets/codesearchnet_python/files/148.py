def setIfMissing(self, key, value):
        """Set a configuration property, if not already set."""
        if self.get(key) is None:
            self.set(key, value)
        return self