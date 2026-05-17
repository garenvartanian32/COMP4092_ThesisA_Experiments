def setParams(self, inputCol=None, outputCol=None, stopWords=None, caseSensitive=False,
                  locale=None):
        """
        setParams(self, inputCol=None, outputCol=None, stopWords=None, caseSensitive=false, \
        locale=None)
        Sets params for this StopWordRemover.
        """
        kwargs = self._input_kwargs
        return self._set(**kwargs)