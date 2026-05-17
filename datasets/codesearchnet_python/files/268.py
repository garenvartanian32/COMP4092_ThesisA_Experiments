def union(self, other):
        """ Return a new :class:`DataFrame` containing union of rows in this and another frame.

        This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union
        (that does deduplication of elements), use this function followed by :func:`distinct`.

        Also as standard in SQL, this function resolves columns by position (not by name).
        """
        return DataFrame(self._jdf.union(other._jdf), self.sql_ctx)