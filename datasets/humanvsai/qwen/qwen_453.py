def remove(self, key):
    if key in self.namespace:
        del self.namespace[key]
    else:
        pass