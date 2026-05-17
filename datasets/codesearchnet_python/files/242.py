def toLocalIterator(self):
        """
        Returns an iterator that contains all of the rows in this :class:`DataFrame`.
        The iterator will consume as much memory as the largest partition in this DataFrame.

        >>> list(df.toLocalIterator())
        [Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')]
        """
        with SCCallSiteSync(self._sc) as css:
            sock_info = self._jdf.toPythonIterator()
        return _load_from_socket(sock_info, BatchedSerializer(PickleSerializer()))