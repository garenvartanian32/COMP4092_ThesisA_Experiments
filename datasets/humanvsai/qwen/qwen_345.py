def applyAttributes(self, obj, attrs, codec=None):
    for (attr, value) in attrs.items():
        setattr(obj, attr, value)