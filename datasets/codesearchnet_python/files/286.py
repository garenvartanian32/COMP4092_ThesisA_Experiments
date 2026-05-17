def transform(self, func):
        """Returns a new class:`DataFrame`. Concise syntax for chaining custom transformations.

        :param func: a function that takes and returns a class:`DataFrame`.

        >>> from pyspark.sql.functions import col
        >>> df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])
        >>> def cast_all_to_int(input_df):
        ...     return input_df.select([col(col_name).cast("int") for col_name in input_df.columns])
        >>> def sort_columns_asc(input_df):
        ...     return input_df.select(*sorted(input_df.columns))
        >>> df.transform(cast_all_to_int).transform(sort_columns_asc).show()
        +-----+---+
        |float|int|
        +-----+---+
        |    1|  1|
        |    2|  2|
        +-----+---+
        """
        result = func(self)
        assert isinstance(result, DataFrame), "Func returned an instance of type [%s], " \
                                              "should have been DataFrame." % type(result)
        return result