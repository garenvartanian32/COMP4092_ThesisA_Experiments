class Battery:
    def __init__(self, current):
        self.current = current

    def measured_current(self):
        """The measured current that the battery is supplying (in microamps)"""
        return self.current