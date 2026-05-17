class Scope:
    def __init__(self):
        self.vars = {}

    def add_var(self, name, value):
        self.vars[name] = value

    def get_var(self, name, recurse=True):
        if name in self.vars:
            return self.vars[name]
        elif recurse:
            # If recursion is allowed, you might need to check the parent scope
            # This is just a placeholder, you'll need to implement this part
            return self.parent.get_var(name)
        else:
            raise ValueError(f"Variable {name} not found")