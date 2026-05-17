def crossJoin(self, other):
        """Returns the cartesian product with another :class:`DataFrame`.

        :param other: Right side of the cartesian product.

        >>> df.select("age", "name").collect()
        [Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')]
        >>> df2.select("name", "height").collect()
        [Row(name=u'Tom', height=80), Row(name=u'Bob', height=85)]
        >>> df.crossJoin(df2.select("height")).select("age", "name", "height").collect()
        [Row(age=2, name=u'Alice', height=80), Row(age=2, name=u'Alice', height=85),
         Row(age=5, name=u'Bob', height=80), Row(age=5, name=u'Bob', height=85)]
        """

        jdf = self._jdf.crossJoin(other._jdf)
        return DataFrame(jdf, self.sql_ctx)