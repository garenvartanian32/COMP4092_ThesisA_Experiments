def load(self, path=None, format=None, schema=None, **options):
        """Loads data from a data source and returns it as a :class`DataFrame`.

        :param path: optional string or a list of string for file-system backed data sources.
        :param format: optional string for format of the data source. Default to 'parquet'.
        :param schema: optional :class:`pyspark.sql.types.StructType` for the input schema
                       or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).
        :param options: all other string options

        >>> df = spark.read.format("parquet").load('python/test_support/sql/parquet_partitioned',
        ...     opt1=True, opt2=1, opt3='str')
        >>> df.dtypes
        [('name', 'string'), ('year', 'int'), ('month', 'int'), ('day', 'int')]

        >>> df = spark.read.format('json').load(['python/test_support/sql/people.json',
        ...     'python/test_support/sql/people1.json'])
        >>> df.dtypes
        [('age', 'bigint'), ('aka', 'string'), ('name', 'string')]
        """
        if format is not None:
            self.format(format)
        if schema is not None:
            self.schema(schema)
        self.options(**options)
        if isinstance(path, basestring):
            return self._df(self._jreader.load(path))
        elif path is not None:
            if type(path) != list:
                path = [path]
            return self._df(self._jreader.load(self._spark._sc._jvm.PythonUtils.toSeq(path)))
        else:
            return self._df(self._jreader.load())