def intersectAll(self, other):
        """ Return a new :class:`DataFrame` containing rows in both this dataframe and other
        dataframe while preserving duplicates.

        This is equivalent to `INTERSECT ALL` in SQL.
        >>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
        >>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])

        >>> df1.intersectAll(df2).sort("C1", "C2").show()
        +---+---+
        | C1| C2|
        +---+---+
        |  a|  1|
        |  a|  1|
        |  b|  3|
        +---+---+

        Also as standard in SQL, this function resolves columns by position (not by name).
        """
        return DataFrame(self._jdf.intersectAll(other._jdf), self.sql_ctx)