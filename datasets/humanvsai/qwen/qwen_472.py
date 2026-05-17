def _GetSqliteSchema(self, proto_struct_class, prefix=''):
    schema = {}
    for field in proto_struct_class.DESCRIPTOR.fields:
        field_name = prefix + field.name
        converter = self._GetConverter(field)
        schema[field_name] = converter
    return schema