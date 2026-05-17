def replace(self, source, dest):
    for replica in self.replicas:
        if replica == source:
            replica = dest
            break