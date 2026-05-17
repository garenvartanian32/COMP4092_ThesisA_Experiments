def open_out_endpoint(usb_device):
    return usb_device.get_active_configuration().interfaces()[0].endpoints()[0].open()
