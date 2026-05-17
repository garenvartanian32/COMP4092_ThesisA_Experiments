class ValidationError(Exception):
    pass

def validate_language_key(obj):
    if isinstance(obj, dict):
        if 'language' not in obj:
            raise ValidationError('"language" key not found')
        for value in obj.values():
            validate_language_key(value)
    elif isinstance(obj, list):
        for item in obj:
            validate_language_key(item)