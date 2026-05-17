def get_index_text(self, obj):
    """Return text for index entry based on object type."""
    obj_type = type(obj)
    if obj_type == int:
        return "This is an integer."
    elif obj_type == str:
        return "This is a string."
    elif obj_type == list:
        return "This is a list."
    else:
        return "This is an unknown type."