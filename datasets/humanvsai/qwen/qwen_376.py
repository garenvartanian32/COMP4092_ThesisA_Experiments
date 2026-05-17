def writeNSdict(self, nsdict):
    for (prefix, uri) in nsdict.items():
        if prefix in self.reserved_prefixes:
            raise ValueError(f"Prefix '{prefix}' is reserved and cannot be used.")
        self.namespaces[prefix] = uri