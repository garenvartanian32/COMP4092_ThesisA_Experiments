def to_arrow_type(dt):
    """ Convert Spark data type to pyarrow type
    """
    import pyarrow as pa
    if type(dt) == BooleanType:
        arrow_type = pa.bool_()
    elif type(dt) == ByteType:
        arrow_type = pa.int8()
    elif type(dt) == ShortType:
        arrow_type = pa.int16()
    elif type(dt) == IntegerType:
        arrow_type = pa.int32()
    elif type(dt) == LongType:
        arrow_type = pa.int64()
    elif type(dt) == FloatType:
        arrow_type = pa.float32()
    elif type(dt) == DoubleType:
        arrow_type = pa.float64()
    elif type(dt) == DecimalType:
        arrow_type = pa.decimal128(dt.precision, dt.scale)
    elif type(dt) == StringType:
        arrow_type = pa.string()
    elif type(dt) == BinaryType:
        arrow_type = pa.binary()
    elif type(dt) == DateType:
        arrow_type = pa.date32()
    elif type(dt) == TimestampType:
        # Timestamps should be in UTC, JVM Arrow timestamps require a timezone to be read
        arrow_type = pa.timestamp('us', tz='UTC')
    elif type(dt) == ArrayType:
        if type(dt.elementType) in [StructType, TimestampType]:
            raise TypeError("Unsupported type in conversion to Arrow: " + str(dt))
        arrow_type = pa.list_(to_arrow_type(dt.elementType))
    elif type(dt) == StructType:
        if any(type(field.dataType) == StructType for field in dt):
            raise TypeError("Nested StructType not supported in conversion to Arrow")
        fields = [pa.field(field.name, to_arrow_type(field.dataType), nullable=field.nullable)
                  for field in dt]
        arrow_type = pa.struct(fields)
    else:
        raise TypeError("Unsupported type in conversion to Arrow: " + str(dt))
    return arrow_type