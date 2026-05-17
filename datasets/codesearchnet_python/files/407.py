def _set_opts(self, schema=None, **options):
        """
        Set named options (filter out those the value is None)
        """
        if schema is not None:
            self.schema(schema)
        for k, v in options.items():
            if v is not None:
                self.option(k, v)