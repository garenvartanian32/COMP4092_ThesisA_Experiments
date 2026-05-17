def path(self):
        return pathlib.Path(self.package.__file__).resolve().parent.parent