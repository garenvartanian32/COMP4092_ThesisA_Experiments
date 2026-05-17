def set_common_entities(self):
    common_entities = {}
    for variable in self.variables:
        if common_entities:
            common_entities = {k: v for k, v in common_entities.items() if k in variable.entities}
        else:
            common_entities = variable.entities
    self.entities = common_entities
