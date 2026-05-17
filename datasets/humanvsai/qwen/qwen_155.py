def populate(self):
    for view in self.views:
        if not view.args:
            self.append(view)