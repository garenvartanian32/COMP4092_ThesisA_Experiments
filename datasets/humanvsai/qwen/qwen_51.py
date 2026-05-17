def out_endpoint(self):
    self._out_endpoint = self._device.open_endpoint(self._out_endpoint_address)
    return self._out_endpoint

def in_endpoint(self):
    """Open a reference to the USB device's only IN endpoint. This method
        assumes that the USB device configuration has already been set."""
    self._in_endpoint = self._device.open_endpoint(self._in_endpoint_address)
    return self._in_endpoint