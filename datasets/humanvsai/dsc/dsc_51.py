import usb.core
import usb.util

# Find the device
device = usb.core.find(idVendor=0x0403, idProduct=0x6001)

# Make sure the device was found
if device is None:
    raise ValueError('Device not found')

# Set the active configuration. With no arguments, the first
# configuration will be the active one
device.set_configuration()

# Get an OUT endpoint instance
cfg = device.get_active_configuration()
interface = cfg[(0,0)]

endpoint = usb.util.find_descriptor(
    interface,
    # Match the first OUT endpoint
    custom_match = \
    lambda e: \
    usb.util.endpoint_direction(e.bEndpointAddress) == \
    usb.util.ENDPOINT_OUT
)

if endpoint is None:
    raise ValueError('Endpoint not found')