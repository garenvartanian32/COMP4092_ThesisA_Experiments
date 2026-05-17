def withColumn(self, colName, col):
        """
        Returns a new :class:`DataFrame` by adding a column or replacing the
        existing column that has the same name.

        The column expression must be an expression over this DataFrame; attempting to add
        a column from some other dataframe will raise an error.

        :param colName: string, name of the new column.
        :param col: a :class:`Column` expression for the new column.

        .. note:: This method introduces a projection internally. Therefore, calling it multiple
            times, for instance, via loops in order to add multiple columns can generate big
            plans which can cause performance issues and even `StackOverflowException`.
            To avoid this, use :func:`select` with the multiple columns at once.

        >>> df.withColumn('age2', df.age + 2).collect()
        [Row(age=2, name=u'Alice', age2=4), Row(age=5, name=u'Bob', age2=7)]

        """
        assert isinstance(col, Column), "col should be Column"
        return DataFrame(self._jdf.withColumn(colName, col._jc), self.sql_ctx)