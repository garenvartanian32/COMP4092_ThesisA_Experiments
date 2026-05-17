import smbus2

def import_i2c_addresses():
    i2c_devices = []
    try:
        bus = smbus2.SMBus(1)
        for address in range(112, 120):
            try:
                bus.read_byte(address)
                i2c_devices.append(address)
            except:
                pass
    except:
        print("Error accessing I2C bus")
    return i2c_devices
