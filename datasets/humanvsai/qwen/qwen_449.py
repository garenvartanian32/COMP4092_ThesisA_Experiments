def accept(self, deviceId, device):
    self.devices[deviceId] = device
    return self.devices[deviceId]