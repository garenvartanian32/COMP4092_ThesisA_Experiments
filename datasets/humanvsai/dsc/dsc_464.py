def ids(self, content_ids, object_ids):
    """Appends the content and object ids how RETS expects them"""
    # Assuming content_ids and object_ids are lists
    return [f'{content_id}:{object_id}' for content_id, object_id in zip(content_ids, object_ids)]