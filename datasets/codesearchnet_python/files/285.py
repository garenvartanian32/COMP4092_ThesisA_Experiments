def toDF(self, *cols):
        """Returns a new class:`DataFrame` that with new specified column names

        :param cols: list of new column names (string)

        >>> df.toDF('f1', 'f2').collect()
        [Row(f1=2, f2=u'Alice'), Row(f1=5, f2=u'Bob')]
        """
        jdf = self._jdf.toDF(self._jseq(cols))
        return DataFrame(jdf, self.sql_ctx)