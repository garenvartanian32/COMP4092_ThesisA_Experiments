def to_dict(self, search_fields=None):
    data = {}
    for key, value in self.__dict__.items():
        if value is not None:
            data[key] = value
    return data