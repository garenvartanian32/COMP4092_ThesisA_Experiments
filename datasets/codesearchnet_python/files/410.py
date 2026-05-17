def option(self, key, value):
        """Adds an input option for the underlying data source.

        You can set the following option(s) for reading files:
            * ``timeZone``: sets the string that indicates a timezone to be used to parse timestamps
                in the JSON/CSV datasources or partition values.
                If it isn't set, it uses the default value, session local timezone.
        """
        self._jreader = self._jreader.option(key, to_str(value))
        return self