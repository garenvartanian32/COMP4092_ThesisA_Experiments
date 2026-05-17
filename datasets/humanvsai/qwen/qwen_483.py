def system_lookup(self, name):
    """lookup a symbol system wide"""
    pass

def add_symbol(self, name, value):
    """add a symbol to the local symbol table"""
    self.symbols[name] = value

def remove_symbol(self, name):
    """remove a symbol from the local symbol table"""
    if name in self.symbols:
        del self.symbols[name]
    else:
        raise KeyError(f"Symbol '{name}' not found in local symbol table")

def __init__(self):
    """initialize the symbol table"""
    self.symbols = {}