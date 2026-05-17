def _classnamelist(self, classname, namespace):
    if classname is None:
        return None
    elif isinstance(classname, (str, CIMClassName)):
        classnames = [classname]
        subclasses = self._get_subclass_names(classname, namespace)
        if subclasses:
            classnames.extend(subclasses)
        return classnames
    else:
        raise ValueError("Invalid type for 'classname': %s" % type(classname))