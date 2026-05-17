def resolve_params(obj, params, default=missing):
    param_values = {}
    for name, attr_tpl in iteritems(params):
        attr_name = tpl(str(attr_tpl))
        if attr_name:
            attribute_value = get_value(obj, attr_name, default=default)
            if attribute_value is not missing:
                param_values[name] = attribute_value
            else:
                raise AttributeError(
                    '{attr_name!r} is not a valid '
                    'attribute of {obj!r}'.format(attr_name=attr_name, obj=obj),
                )
        else:
            param_values[name] = attr_tpl
    return param_values