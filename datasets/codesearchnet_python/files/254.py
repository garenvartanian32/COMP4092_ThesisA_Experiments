def alias(self, alias):
        """Returns a new :class:`DataFrame` with an alias set.

        :param alias: string, an alias name to be set for the DataFrame.

        >>> from pyspark.sql.functions import *
        >>> df_as1 = df.alias("df_as1")
        >>> df_as2 = df.alias("df_as2")
        >>> joined_df = df_as1.join(df_as2, col("df_as1.name") == col("df_as2.name"), 'inner')
        >>> joined_df.select("df_as1.name", "df_as2.name", "df_as2.age").collect()
        [Row(name=u'Bob', name=u'Bob', age=5), Row(name=u'Alice', name=u'Alice', age=2)]
        """
        assert isinstance(alias, basestring), "alias should be a string"
        return DataFrame(getattr(self._jdf, "as")(alias), self.sql_ctx)