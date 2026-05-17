def from_arrow_schema(arrow_schema):
    """ Convert schema from Arrow to Spark.
    """
    return StructType(
        [StructField(field.name, from_arrow_type(field.type), nullable=field.nullable)
         for field in arrow_schema])