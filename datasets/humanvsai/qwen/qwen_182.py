def resolve_params(obj, params, default=missing):
    if default is missing:
        default = {}
    resolved_params = {}
    for (key, value) in params.items():
        if isinstance(value, str) and value.startswith('<') and value.endswith('>'):
            attr_name = value[1:-1]
            resolved_params[key] = getattr(obj, attr_name, default.get(key, value))
        else:
            resolved_params[key] = value
    return resolved_params

class Example:

    def __init__(self, name, age):
        self.name = name
        self.age = age
example = Example('Alice', 30)
params = {'greeting': 'Hello, <name>!', 'age': '<age>'}
resolved = resolve_params(example, params)