def _GetSqliteSchema(self, proto_struct_class, prefix=""):
    schema_mapping = {}
    for field in proto_struct_class._meta.fields:
        column_name = prefix + field.column
        converter = field.converter
        schema_mapping[column_name] = converter
    return schema_mapping