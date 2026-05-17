def add_alias(self, alias: sym.Symbol, namespace: "Namespace") -> None:
        self._aliases.swap(lambda m: m.assoc(alias, namespace))