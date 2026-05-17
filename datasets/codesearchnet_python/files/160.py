def createTable(self, tableName, path=None, source=None, schema=None, **options):
        """Creates a table based on the dataset in a data source.

        It returns the DataFrame associated with the table.

        The data source is specified by the ``source`` and a set of ``options``.
        If ``source`` is not specified, the default data source configured by
        ``spark.sql.sources.default`` will be used. When ``path`` is specified, an external table is
        created from the data at the given path. Otherwise a managed table is created.

        Optionally, a schema can be provided as the schema of the returned :class:`DataFrame` and
        created table.

        :return: :class:`DataFrame`
        """
        if path is not None:
            options["path"] = path
        if source is None:
            source = self._sparkSession._wrapped._conf.defaultDataSourceName()
        if schema is None:
            df = self._jcatalog.createTable(tableName, source, options)
        else:
            if not isinstance(schema, StructType):
                raise TypeError("schema should be StructType")
            scala_datatype = self._jsparkSession.parseDataType(schema.json())
            df = self._jcatalog.createTable(tableName, source, scala_datatype, options)
        return DataFrame(df, self._sparkSession._wrapped)