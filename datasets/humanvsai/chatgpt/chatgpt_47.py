def set_attributes(obj, values_dict):
    for key, value in values_dict.items():
        setattr(obj, key, value)
