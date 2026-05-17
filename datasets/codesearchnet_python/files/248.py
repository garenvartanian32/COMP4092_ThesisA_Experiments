def repartition(self, numPartitions, *cols):
        """
        Returns a new :class:`DataFrame` partitioned by the given partitioning expressions. The
        resulting DataFrame is hash partitioned.

        :param numPartitions:
            can be an int to specify the target number of partitions or a Column.
            If it is a Column, it will be used as the first partitioning column. If not specified,
            the default number of partitions is used.

        .. versionchanged:: 1.6
           Added optional arguments to specify the partitioning columns. Also made numPartitions
           optional if partitioning columns are specified.

        >>> df.repartition(10).rdd.getNumPartitions()
        10
        >>> data = df.union(df).repartition("age")
        >>> data.show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  5|  Bob|
        |  2|Alice|
        |  2|Alice|
        +---+-----+
        >>> data = data.repartition(7, "age")
        >>> data.show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        |  5|  Bob|
        |  2|Alice|
        |  5|  Bob|
        +---+-----+
        >>> data.rdd.getNumPartitions()
        7
        >>> data = data.repartition("name", "age")
        >>> data.show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  5|  Bob|
        |  2|Alice|
        |  2|Alice|
        +---+-----+
        """
        if isinstance(numPartitions, int):
            if len(cols) == 0:
                return DataFrame(self._jdf.repartition(numPartitions), self.sql_ctx)
            else:
                return DataFrame(
                    self._jdf.repartition(numPartitions, self._jcols(*cols)), self.sql_ctx)
        elif isinstance(numPartitions, (basestring, Column)):
            cols = (numPartitions, ) + cols
            return DataFrame(self._jdf.repartition(self._jcols(*cols)), self.sql_ctx)
        else:
            raise TypeError("numPartitions should be an int or Column")