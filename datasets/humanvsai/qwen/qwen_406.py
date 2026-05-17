def to_dict(self, search_fields=None):
    if search_fields is None:
        search_fields = self.__dict__.keys()
    result = {}
    for field in search_fields:
        value = getattr(self, field, None)
        if value is not None:
            result[field] = value
    return result