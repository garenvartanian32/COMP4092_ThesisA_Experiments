def AddShadow(self, fileset):
    for file in fileset:
        if file in self.shadow_store:
            self.shadow_store[file] += 1
        else:
            self.shadow_store[file] = 1
    return self.shadow_store