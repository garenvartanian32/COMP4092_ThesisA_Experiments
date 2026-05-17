def _index_entities(self):
    common_entities = {}
    for variable in self.variables:
        variable_entities = variable.get_entities()
        if not common_entities:
            common_entities = variable_entities.copy()
        else:
            common_entities = {key: value for (key, value) in common_entities.items() if key in variable_entities and value == variable_entities[key]}
    self.entities = common_entities