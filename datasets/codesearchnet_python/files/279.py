def cov(self, col1, col2):
        """
        Calculate the sample covariance for the given columns, specified by their names, as a
        double value. :func:`DataFrame.cov` and :func:`DataFrameStatFunctions.cov` are aliases.

        :param col1: The name of the first column
        :param col2: The name of the second column
        """
        if not isinstance(col1, basestring):
            raise ValueError("col1 should be a string.")
        if not isinstance(col2, basestring):
            raise ValueError("col2 should be a string.")
        return self._jdf.stat().cov(col1, col2)