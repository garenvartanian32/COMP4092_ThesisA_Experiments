def append_ids(content_id, object_id):
    """
    Appends the content and object ids how RETS expects them
    
    Args:
    content_id (str): The content id as a string
    object_id (str): The object id as a string
    
    Returns:
    a string containing the content and object ids
    """
    return content_id + ":" + object_id
