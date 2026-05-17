import smbus

def import_i2c_addr(bus, opt="sensors"):
    addresses = []
    for addr in range(112, 120):  # I2C addresses are usually in the range 112-127
        try:
            smbus.SMBus(bus).read_byte(addr)
            addresses.append(addr)
        except:
            pass
    return addresses