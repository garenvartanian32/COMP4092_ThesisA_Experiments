def import_i2c_addr(bus, opt='sensors'):
    import smbus
    bus = smbus.SMBus(bus)
    devices = []
    for device in range(112, 119):
        try:
            bus.read_byte(device)
            devices.append(device)
        except IOError:
            pass
    return devices