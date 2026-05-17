def validate(self, value):
        try:
            coord.Angle(value, unit=self.unit)
            return value
        except ValueError:
            return None