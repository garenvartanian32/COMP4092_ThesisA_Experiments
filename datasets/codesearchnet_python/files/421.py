def option(self, key, value):
        """Adds an output option for the underlying data source.

        You can set the following option(s) for writing files:
            * ``timeZone``: sets the string that indicates a timezone to be used to format
                timestamps in the JSON/CSV datasources or partition values.
                If it isn't set, it uses the default value, session local timezone.
        """
        self._jwrite = self._jwrite.option(key, to_str(value))
        return self