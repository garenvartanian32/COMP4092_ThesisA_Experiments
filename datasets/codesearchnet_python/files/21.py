def from_arrow_type(at):
    """ Convert pyarrow type to Spark data type.
    """
    import pyarrow.types as types
    if types.is_boolean(at):
        spark_type = BooleanType()
    elif types.is_int8(at):
        spark_type = ByteType()
    elif types.is_int16(at):
        spark_type = ShortType()
    elif types.is_int32(at):
        spark_type = IntegerType()
    elif types.is_int64(at):
        spark_type = LongType()
    elif types.is_float32(at):
        spark_type = FloatType()
    elif types.is_float64(at):
        spark_type = DoubleType()
    elif types.is_decimal(at):
        spark_type = DecimalType(precision=at.precision, scale=at.scale)
    elif types.is_string(at):
        spark_type = StringType()
    elif types.is_binary(at):
        spark_type = BinaryType()
    elif types.is_date32(at):
        spark_type = DateType()
    elif types.is_timestamp(at):
        spark_type = TimestampType()
    elif types.is_list(at):
        if types.is_timestamp(at.value_type):
            raise TypeError("Unsupported type in conversion from Arrow: " + str(at))
        spark_type = ArrayType(from_arrow_type(at.value_type))
    elif types.is_struct(at):
        if any(types.is_struct(field.type) for field in at):
            raise TypeError("Nested StructType not supported in conversion from Arrow: " + str(at))
        return StructType(
            [StructField(field.name, from_arrow_type(field.type), nullable=field.nullable)
             for field in at])
    else:
        raise TypeError("Unsupported type in conversion from Arrow: " + str(at))
    return spark_type