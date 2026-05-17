def out_endpoint(self):
        if getattr(self, '_out_endpoint', None) is None:
            config = self.device.get_active_configuration()
            interface_number = config[(0, 0)].bInterfaceNumber
            interface = usb.util.find_descriptor(config,
                    bInterfaceNumber=interface_number)
            self._out_endpoint = usb.util.find_descriptor(interface,
                    custom_match = \
                            lambda e: \
                            usb.util.endpoint_direction(e.bEndpointAddress) == \
                            usb.util.ENDPOINT_OUT)
            if not self._out_endpoint:
                raise ControllerError(
                        "Couldn't find OUT endpoint on the USB device")
        return self._out_endpoint