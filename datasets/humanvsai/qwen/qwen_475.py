def get_var(self, name, recurse=True):
    if recurse:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
    elif name in self.scopes[-1]:
        return self.scopes[-1][name]
    return None