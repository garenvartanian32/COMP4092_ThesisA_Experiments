def validate_language_key(obj, key):
    if isinstance(obj, dict):
        for (k, v) in obj.items():
            if k == 'language':
                if v not in ['en', 'fr', 'es', 'de']:
                    raise ValidationError(f'Invalid language code: {v}')
            else:
                validate_language_key(v, key)
    elif isinstance(obj, list):
        for item in obj:
            validate_language_key(item, key)

class ValidationError(Exception):
    pass
data = {'name': 'John', 'details': {'language': 'en', 'age': 30}, 'hobbies': [{'name': 'reading', 'language': 'fr'}, {'name': 'traveling', 'language': 'es'}]}