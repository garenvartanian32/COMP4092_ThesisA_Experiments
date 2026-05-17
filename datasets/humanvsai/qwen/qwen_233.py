def parse_content_type_header(value):
    parts = value.split('/', 1)
    if len(parts) != 2:
        raise ValueError('Invalid content type header format')
    (maintype, subtype) = parts
    parameters = {}
    if ';' in subtype:
        (subtype, params_str) = subtype.split(';', 1)
        params = params_str.split(';')
        for param in params:
            (key, value) = param.split('=', 1)
            parameters[key.strip()] = value.strip()
    return (maintype.strip(), subtype.strip(), parameters)
content_type = 'text/html; charset=utf-8'
(maintype, subtype, params) = parse_content_type_header(content_type)