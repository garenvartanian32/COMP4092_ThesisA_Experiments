def sortWithinPartitions(self, *cols, **kwargs):
        """Returns a new :class:`DataFrame` with each partition sorted by the specified column(s).

        :param cols: list of :class:`Column` or column names to sort by.
        :param ascending: boolean or list of boolean (default True).
            Sort ascending vs. descending. Specify list for multiple sort orders.
            If a list is specified, length of the list must equal length of the `cols`.

        >>> df.sortWithinPartitions("age", ascending=False).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        |  5|  Bob|
        +---+-----+
        """
        jdf = self._jdf.sortWithinPartitions(self._sort_cols(cols, kwargs))
        return DataFrame(jdf, self.sql_ctx)