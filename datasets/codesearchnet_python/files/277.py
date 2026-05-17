def approxQuantile(self, col, probabilities, relativeError):
        """
        Calculates the approximate quantiles of numerical columns of a
        DataFrame.

        The result of this algorithm has the following deterministic bound:
        If the DataFrame has N elements and if we request the quantile at
        probability `p` up to error `err`, then the algorithm will return
        a sample `x` from the DataFrame so that the *exact* rank of `x` is
        close to (p * N). More precisely,

          floor((p - err) * N) <= rank(x) <= ceil((p + err) * N).

        This method implements a variation of the Greenwald-Khanna
        algorithm (with some speed optimizations). The algorithm was first
        present in [[https://doi.org/10.1145/375663.375670
        Space-efficient Online Computation of Quantile Summaries]]
        by Greenwald and Khanna.

        Note that null values will be ignored in numerical columns before calculation.
        For columns only containing null values, an empty list is returned.

        :param col: str, list.
          Can be a single column name, or a list of names for multiple columns.
        :param probabilities: a list of quantile probabilities
          Each number must belong to [0, 1].
          For example 0 is the minimum, 0.5 is the median, 1 is the maximum.
        :param relativeError:  The relative target precision to achieve
          (>= 0). If set to zero, the exact quantiles are computed, which
          could be very expensive. Note that values greater than 1 are
          accepted but give the same result as 1.
        :return:  the approximate quantiles at the given probabilities. If
          the input `col` is a string, the output is a list of floats. If the
          input `col` is a list or tuple of strings, the output is also a
          list, but each element in it is a list of floats, i.e., the output
          is a list of list of floats.

        .. versionchanged:: 2.2
           Added support for multiple columns.
        """

        if not isinstance(col, (basestring, list, tuple)):
            raise ValueError("col should be a string, list or tuple, but got %r" % type(col))

        isStr = isinstance(col, basestring)

        if isinstance(col, tuple):
            col = list(col)
        elif isStr:
            col = [col]

        for c in col:
            if not isinstance(c, basestring):
                raise ValueError("columns should be strings, but got %r" % type(c))
        col = _to_list(self._sc, col)

        if not isinstance(probabilities, (list, tuple)):
            raise ValueError("probabilities should be a list or tuple")
        if isinstance(probabilities, tuple):
            probabilities = list(probabilities)
        for p in probabilities:
            if not isinstance(p, (float, int, long)) or p < 0 or p > 1:
                raise ValueError("probabilities should be numerical (float, int, long) in [0,1].")
        probabilities = _to_list(self._sc, probabilities)

        if not isinstance(relativeError, (float, int, long)) or relativeError < 0:
            raise ValueError("relativeError should be numerical (float, int, long) >= 0.")
        relativeError = float(relativeError)

        jaq = self._jdf.stat().approxQuantile(col, probabilities, relativeError)
        jaq_list = [list(j) for j in jaq]
        return jaq_list[0] if isStr else jaq_list