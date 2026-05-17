def subtract(self, other):
        """ Return a new :class:`DataFrame` containing rows in this frame
        but not in another frame.

        This is equivalent to `EXCEPT DISTINCT` in SQL.

        """
        return DataFrame(getattr(self._jdf, "except")(other._jdf), self.sql_ctx)