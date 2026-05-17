class SymbolLookup:
    def __init__(self):
        self.local_symbols = {}  # local symbols
        self.system_symbols = {}  # system wide symbols

    def lookup(self, name):
        """lookup a symbol by name. If symbol is not local
        it will be looked up system wide"""
        if name in self.local_symbols:
            return self.local_symbols[name]
        elif name in self.system_symbols:
            return self.system_symbols[name]
        else:
            raise ValueError(f"Symbol {name} not found")