import re

def resolve_params(obj, params, default=None):
    """Given a dictionary of keyword arguments, return the same dictionary except with
    values enclosed in `< >` resolved to attributes on `obj`."""
    pattern = re.compile(r'<(.*?)>')
    resolved_params = {}
    for key, value in params.items():
        if isinstance(value, str):
            matches = pattern.findall(value)
            for match in matches:
                if hasattr(obj, match):
                    value = value.replace('<' + match + '>', str(getattr(obj, match)))
                elif default is not None:
                    value = value.replace('<' + match + '>', str(default))
            resolved_params[key] = value
        else:
            resolved_params[key] = value
    return resolved_params