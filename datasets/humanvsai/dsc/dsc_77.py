class YourClassName:
    def options(self, **options):
        """Adds input options for the underlying data source."""
        if 'timeZone' in options:
            self.timeZone = options['timeZone']
        else:
            self.timeZone = 'default_timezone'  # replace with your default timezone