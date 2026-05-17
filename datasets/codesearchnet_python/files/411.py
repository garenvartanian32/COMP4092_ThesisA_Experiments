def options(self, **options):
        """Adds input options for the underlying data source.

        You can set the following option(s) for reading files:
            * ``timeZone``: sets the string that indicates a timezone to be used to parse timestamps
                in the JSON/CSV datasources or partition values.
                If it isn't set, it uses the default value, session local timezone.
        """
        for k in options:
            self._jreader = self._jreader.option(k, to_str(options[k]))
        return self