def parse_content_type_header(value):
    maintype, subtype = value.split(';')[0].split('/')
    params = dict(param.split('=') for param in value[len(maintype + '/' + subtype):].strip().split(';'))
    return maintype, subtype, params