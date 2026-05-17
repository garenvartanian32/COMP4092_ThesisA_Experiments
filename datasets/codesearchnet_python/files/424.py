def sortBy(self, col, *cols):
        """Sorts the output in each bucket by the given columns on the file system.

        :param col: a name of a column, or a list of names.
        :param cols: additional names (optional). If `col` is a list it should be empty.

        >>> (df.write.format('parquet')  # doctest: +SKIP
        ...     .bucketBy(100, 'year', 'month')
        ...     .sortBy('day')
        ...     .mode("overwrite")
        ...     .saveAsTable('sorted_bucketed_table'))
        """
        if isinstance(col, (list, tuple)):
            if cols:
                raise ValueError("col is a {0} but cols are not empty".format(type(col)))

            col, cols = col[0], col[1:]

        if not all(isinstance(c, basestring) for c in cols) or not(isinstance(col, basestring)):
            raise TypeError("all names should be `str`")

        self._jwrite = self._jwrite.sortBy(col, _to_seq(self._spark._sc, cols))
        return self