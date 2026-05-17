def measured_current(self):
    return self._measured_current

def measured_voltage(self):
    """The measured voltage that the battery is supplying (in millivolts)"""
    return self._measured_voltage

def measured_power(self):
    """The measured power that the battery is supplying (in microwatts)"""
    return self._measured_power

def update_measurements(self, current, voltage, power):
    """Update the measured current, voltage, and power of the battery."""
    self._measured_current = current
    self._measured_current = voltage
    self._measured_power = power

def display_measurements(self):
    """Display the current, voltage, and power measurements."""
    print(f'Current: {self._measured_current} microamps')
    print(f'Voltage: {self._measured_voltage} millivolts')
    print(f'Power: {self._measured_power} microwatts')