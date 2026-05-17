def measured_current(self):
        self._measured_current, value = self.get_attr_int(self._measured_current, 'current_now')
        return value