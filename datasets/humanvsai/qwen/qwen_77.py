def options(self, **options):

    def set_option(self, key, value):
        """Sets a single option."""
        self._options[key] = value
    for (key, value) in options.items():
        set_option(key, value)
    return self