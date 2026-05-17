def toDebugString(self):
        """
        Returns a printable version of the configuration, as a list of
        key=value pairs, one per line.
        """
        if self._jconf is not None:
            return self._jconf.toDebugString()
        else:
            return '\n'.join('%s=%s' % (k, v) for k, v in self._conf.items())