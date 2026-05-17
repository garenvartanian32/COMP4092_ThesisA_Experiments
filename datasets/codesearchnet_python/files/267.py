def groupBy(self, *cols):
        """Groups the :class:`DataFrame` using the specified columns,
        so we can run aggregation on them. See :class:`GroupedData`
        for all the available aggregate functions.

        :func:`groupby` is an alias for :func:`groupBy`.

        :param cols: list of columns to group by.
            Each element should be a column name (string) or an expression (:class:`Column`).

        >>> df.groupBy().avg().collect()
        [Row(avg(age)=3.5)]
        >>> sorted(df.groupBy('name').agg({'age': 'mean'}).collect())
        [Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]
        >>> sorted(df.groupBy(df.name).avg().collect())
        [Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]
        >>> sorted(df.groupBy(['name', df.age]).count().collect())
        [Row(name=u'Alice', age=2, count=1), Row(name=u'Bob', age=5, count=1)]
        """
        jgd = self._jdf.groupBy(self._jcols(*cols))
        from pyspark.sql.group import GroupedData
        return GroupedData(jgd, self)