def _classnamelist(self, classname, namespace):
    if classname is None:
        return []

    # Get the class object from its name
    class_obj = namespace.get(classname)

    if class_obj is None:
        return None

    # Get all subclasses of the class
    subclasses = class_obj.__subclasses__()

    # Add the class itself to the list
    class_list = [class_obj]

    # Add all subclasses to the list
    class_list.extend(subclasses)

    return class_list