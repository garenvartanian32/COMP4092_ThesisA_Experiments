def withColumnRenamed(self, existing, new):
        """Returns a new :class:`DataFrame` by renaming an existing column.
        This is a no-op if schema doesn't contain the given column name.

        :param existing: string, name of the existing column to rename.
        :param new: string, new name of the column.

        >>> df.withColumnRenamed('age', 'age2').collect()
        [Row(age2=2, name=u'Alice'), Row(age2=5, name=u'Bob')]
        """
        return DataFrame(self._jdf.withColumnRenamed(existing, new), self.sql_ctx)