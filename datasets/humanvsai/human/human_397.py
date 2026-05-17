def validate_language_key(obj, key):
    backend = bigchaindb.config['database']['backend']
    if backend == 'localmongodb':
        data = obj.get(key, {})
        if isinstance(data, dict):
            validate_all_values_for_key_in_obj(data, 'language', validate_language)
        elif isinstance(data, list):
            validate_all_values_for_key_in_list(data, 'language', validate_language)