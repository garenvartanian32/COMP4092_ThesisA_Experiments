def getAll(self):
        """Get all values as a list of key-value pairs."""
        if self._jconf is not None:
            return [(elem._1(), elem._2()) for elem in self._jconf.getAll()]
        else:
            return self._conf.items()