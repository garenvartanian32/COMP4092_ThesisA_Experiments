def set_attributes(d, elm):
    for (key, value) in d.items():
        setattr(elm, key, value)

def get_attributes(d, elm):
    """Get attributes from an object and store them in a dictionary."""
    for key in d.keys():
        d[key] = getattr(elm, key)

class Example:

    def __init__(self):
        self.attr1 = None
        self.attr2 = None
example = Example()
attributes = {'attr1': 10, 'attr2': 20}
retrieved_attributes = {'attr1': None, 'attr2': None}