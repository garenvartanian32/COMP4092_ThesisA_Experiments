class Namespace:
    def __init__(self):
        self.aliases = []

    def add_alias(self, alias: str):
        """Add a Symbol alias for the given Namespace."""
        self.aliases.append(alias)