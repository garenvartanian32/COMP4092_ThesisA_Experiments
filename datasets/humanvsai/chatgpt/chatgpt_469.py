def resolve_variables(provided_variables):
    for variable in provided_variables:
        if variable.value_from:
            value = variable.value_from.resolve()
            variable.value = value
    return provided_variables
