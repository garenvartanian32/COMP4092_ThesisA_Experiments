def set_status(self, name):
    if name is None:
        self.status = None
    else:
        self.status = name