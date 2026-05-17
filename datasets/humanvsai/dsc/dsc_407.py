class Device:
    def __init__(self, device_type, device_id):
        self.device_type = device_type
        self.device_id = device_id

def newDevice(device_type, device_id):
    """Create new device object for the given type."""
    return Device(device_type, device_id)