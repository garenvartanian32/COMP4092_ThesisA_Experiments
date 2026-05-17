def replace(self, source, dest):
        for i, broker in enumerate(self.replicas):
            if broker == source:
                self.replicas[i] = dest
                return