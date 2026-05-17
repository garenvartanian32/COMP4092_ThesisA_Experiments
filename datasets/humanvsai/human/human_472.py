def _GetSqliteSchema(self, proto_struct_class, prefix=""):
    schema = collections.OrderedDict()
    for type_info in proto_struct_class.type_infos:
      if type_info.__class__ is rdf_structs.ProtoEmbedded:
        schema.update(
            self._GetSqliteSchema(
                type_info.type, prefix="%s%s." % (prefix, type_info.name)))
      else:
        field_name = utils.SmartStr(prefix + type_info.name)
        schema[field_name] = Rdf2SqliteAdapter.GetConverter(type_info)
    return schema