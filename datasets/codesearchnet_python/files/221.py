def setParams(self, minSupport=0.1, maxPatternLength=10, maxLocalProjDBSize=32000000,
                  sequenceCol="sequence"):
        """
        setParams(self, minSupport=0.1, maxPatternLength=10, maxLocalProjDBSize=32000000, \
                  sequenceCol="sequence")
        """
        kwargs = self._input_kwargs
        return self._set(**kwargs)