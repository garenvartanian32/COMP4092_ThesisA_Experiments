def _checkType(self, obj, identifier):
        """Assert that an object is of type str."""
        if not isinstance(obj, basestring):
            raise TypeError("expected %s '%s' to be a string (was '%s')" %
                            (identifier, obj, type(obj).__name__))