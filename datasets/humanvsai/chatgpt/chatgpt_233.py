def parse_content_type(content_type):
    content_type = content_type.strip()
    if not content_type:
        return None
    parts = content_type.split(';')
    main_subtype = parts.pop(0).strip()
    if '/' not in main_subtype:
        return None
    maintype, subtype = main_subtype.split('/', 1)
    parameters = {}
    for part in parts:
        if '=' in part:
            name, value = part.split('=', 1)
            parameters[name.strip()] = value.strip()
    return maintype, subtype, parameters
