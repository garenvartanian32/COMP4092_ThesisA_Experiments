def options(self, **options):
        for k in options:
            self._jreader = self._jreader.option(k, to_str(options[k]))
        return self