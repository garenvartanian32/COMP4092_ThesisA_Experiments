def generate_dependencies(self):
        self.create_variable_is_dict()
        with self.l('if {variable}_is_dict:'):
            self.create_variable_keys()
            for key, values in self._definition["dependencies"].items():
                if values == [] or values is True:
                    continue
                with self.l('if "{}" in {variable}_keys:', key):
                    if values is False:
                        self.l('raise JsonSchemaException("{} in {name} must not be there")', key)
                    elif isinstance(values, list):
                        for value in values:
                            with self.l('if "{}" not in {variable}_keys:', value):
                                self.l('raise JsonSchemaException("{name} missing dependency {} for {}")', value, key)
                    else:
                        self.generate_func_code_block(values, self._variable, self._variable_name, clear_variables=True)