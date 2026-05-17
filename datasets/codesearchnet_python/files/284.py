def drop(self, *cols):
        """Returns a new :class:`DataFrame` that drops the specified column.
        This is a no-op if schema doesn't contain the given column name(s).

        :param cols: a string name of the column to drop, or a
            :class:`Column` to drop, or a list of string name of the columns to drop.

        >>> df.drop('age').collect()
        [Row(name=u'Alice'), Row(name=u'Bob')]

        >>> df.drop(df.age).collect()
        [Row(name=u'Alice'), Row(name=u'Bob')]

        >>> df.join(df2, df.name == df2.name, 'inner').drop(df.name).collect()
        [Row(age=5, height=85, name=u'Bob')]

        >>> df.join(df2, df.name == df2.name, 'inner').drop(df2.name).collect()
        [Row(age=5, name=u'Bob', height=85)]

        >>> df.join(df2, 'name', 'inner').drop('age', 'height').collect()
        [Row(name=u'Bob')]
        """
        if len(cols) == 1:
            col = cols[0]
            if isinstance(col, basestring):
                jdf = self._jdf.drop(col)
            elif isinstance(col, Column):
                jdf = self._jdf.drop(col._jc)
            else:
                raise TypeError("col should be a string or a Column")
        else:
            for col in cols:
                if not isinstance(col, basestring):
                    raise TypeError("each col in the param list should be a string")
            jdf = self._jdf.drop(self._jseq(cols))

        return DataFrame(jdf, self.sql_ctx)