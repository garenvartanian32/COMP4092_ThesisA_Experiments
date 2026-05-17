def get_index_entry_text(obj):
    if isinstance(obj, str):
        return obj.lower()
    elif isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, float):
        return '{:.2f}'.format(obj)
    elif isinstance(obj, list):
        return ', '.join(map(str, obj))
    elif isinstance(obj, dict):
        return ', '.join('{}={}'.format(k, v) for k, v in obj.items())
    else:
        return str(obj)
