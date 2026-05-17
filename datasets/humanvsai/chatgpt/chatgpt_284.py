def load_json_from_storage(storage_object):
    json_data = None
    if storage_object is not None and 'json' in storage_object:
        json_data = storage_object['json']
    return json_data
