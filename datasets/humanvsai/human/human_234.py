def _classnamelist(self, classname, namespace):
        if not classname:
            return []
        cn = classname.classname if isinstance(classname, CIMClassName) \
            else classname
        result = self._get_subclass_names(cn, namespace, True)
        result.append(classname)
        return result