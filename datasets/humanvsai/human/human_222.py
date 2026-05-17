def add_record(self, schema, _bump_stack_level=False):
        full_name = get_full_name(schema)
        has_namespace = '.' in full_name
        self._force_add(full_name, schema, _bump_stack_level, _raise_on_existing=has_namespace)
        if has_namespace and schema.__name__ not in self._schema_map:
            self._force_add(schema.__name__, schema, _bump_stack_level)
        return schema