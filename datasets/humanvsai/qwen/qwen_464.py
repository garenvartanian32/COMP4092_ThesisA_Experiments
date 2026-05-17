def ids(self, content_ids, object_ids):
    content_ids = [str(id) for id in content_ids]
    object_ids = [str(id) for id in object_ids]
    content_ids_str = ','.join(content_ids)
    object_ids_str = ','.join(object_ids)
    return f'{content_ids_str}|{object_ids_str}'