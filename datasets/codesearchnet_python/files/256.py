def join(self, other, on=None, how=None):
        """Joins with another :class:`DataFrame`, using the given join expression.

        :param other: Right side of the join
        :param on: a string for the join column name, a list of column names,
            a join expression (Column), or a list of Columns.
            If `on` is a string or a list of strings indicating the name of the join column(s),
            the column(s) must exist on both sides, and this performs an equi-join.
        :param how: str, default ``inner``. Must be one of: ``inner``, ``cross``, ``outer``,
            ``full``, ``fullouter``, ``full_outer``, ``left``, ``leftouter``, ``left_outer``,
            ``right``, ``rightouter``, ``right_outer``, ``semi``, ``leftsemi``, ``left_semi``,
            ``anti``, ``leftanti`` and ``left_anti``.

        The following performs a full outer join between ``df1`` and ``df2``.

        >>> df.join(df2, df.name == df2.name, 'outer').select(df.name, df2.height).collect()
        [Row(name=None, height=80), Row(name=u'Bob', height=85), Row(name=u'Alice', height=None)]

        >>> df.join(df2, 'name', 'outer').select('name', 'height').collect()
        [Row(name=u'Tom', height=80), Row(name=u'Bob', height=85), Row(name=u'Alice', height=None)]

        >>> cond = [df.name == df3.name, df.age == df3.age]
        >>> df.join(df3, cond, 'outer').select(df.name, df3.age).collect()
        [Row(name=u'Alice', age=2), Row(name=u'Bob', age=5)]

        >>> df.join(df2, 'name').select(df.name, df2.height).collect()
        [Row(name=u'Bob', height=85)]

        >>> df.join(df4, ['name', 'age']).select(df.name, df.age).collect()
        [Row(name=u'Bob', age=5)]
        """

        if on is not None and not isinstance(on, list):
            on = [on]

        if on is not None:
            if isinstance(on[0], basestring):
                on = self._jseq(on)
            else:
                assert isinstance(on[0], Column), "on should be Column or list of Column"
                on = reduce(lambda x, y: x.__and__(y), on)
                on = on._jc

        if on is None and how is None:
            jdf = self._jdf.join(other._jdf)
        else:
            if how is None:
                how = "inner"
            if on is None:
                on = self._jseq([])
            assert isinstance(how, basestring), "how should be basestring"
            jdf = self._jdf.join(other._jdf, on, how)
        return DataFrame(jdf, self.sql_ctx)