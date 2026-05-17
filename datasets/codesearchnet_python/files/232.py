def schema(self):
        """Returns the schema of this :class:`DataFrame` as a :class:`pyspark.sql.types.StructType`.

        >>> df.schema
        StructType(List(StructField(age,IntegerType,true),StructField(name,StringType,true)))
        """
        if self._schema is None:
            try:
                self._schema = _parse_datatype_json_string(self._jdf.schema().json())
            except AttributeError as e:
                raise Exception(
                    "Unable to parse datatype from schema. %s" % e)
        return self._schema