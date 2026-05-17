def colRegex(self, colName):
        """
        Selects column based on the column name specified as a regex and returns it
        as :class:`Column`.

        :param colName: string, column name specified as a regex.

        >>> df = spark.createDataFrame([("a", 1), ("b", 2), ("c",  3)], ["Col1", "Col2"])
        >>> df.select(df.colRegex("`(Col1)?+.+`")).show()
        +----+
        |Col2|
        +----+
        |   1|
        |   2|
        |   3|
        +----+
        """
        if not isinstance(colName, basestring):
            raise ValueError("colName should be provided as string")
        jc = self._jdf.colRegex(colName)
        return Column(jc)