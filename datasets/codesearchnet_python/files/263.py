def head(self, n=None):
        """Returns the first ``n`` rows.

        .. note:: This method should only be used if the resulting array is expected
            to be small, as all the data is loaded into the driver's memory.

        :param n: int, default 1. Number of rows to return.
        :return: If n is greater than 1, return a list of :class:`Row`.
            If n is 1, return a single Row.

        >>> df.head()
        Row(age=2, name=u'Alice')
        >>> df.head(1)
        [Row(age=2, name=u'Alice')]
        """
        if n is None:
            rs = self.head(1)
            return rs[0] if rs else None
        return self.take(n)