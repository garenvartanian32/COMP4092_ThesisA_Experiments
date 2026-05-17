def schema(self, schema):
        """Specifies the input schema.

        Some data sources (e.g. JSON) can infer the input schema automatically from data.
        By specifying the schema here, the underlying data source can skip the schema
        inference step, and thus speed up data loading.

        :param schema: a :class:`pyspark.sql.types.StructType` object or a DDL-formatted string
                       (For example ``col0 INT, col1 DOUBLE``).

        >>> s = spark.read.schema("col0 INT, col1 DOUBLE")
        """
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
        if isinstance(schema, StructType):
            jschema = spark._jsparkSession.parseDataType(schema.json())
            self._jreader = self._jreader.schema(jschema)
        elif isinstance(schema, basestring):
            self._jreader = self._jreader.schema(schema)
        else:
            raise TypeError("schema should be StructType or string")
        return self