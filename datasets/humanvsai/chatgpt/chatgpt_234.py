def build_class_list(classname):
    if classname is None:
        return []
    elif isinstance(classname, str):
        class_list = [classname]
        for subclass in classname.__subclasses__():
            class_list += build_class_list(subclass)
        return class_list
    else:
        raise TypeError("classname should be str or None")
