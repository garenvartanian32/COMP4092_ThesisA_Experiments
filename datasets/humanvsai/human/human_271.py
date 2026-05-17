def import_i2c_addr(bus, opt="sensors"):
    i2c_list = []
    for device in range(128):
        try:
            bus.read_byte(device)
            i2c_list.append((device))
        except IOError:
            pass

    if opt == "sensors":
        sensor_list = []
        for module in range(112,120):
            try:
                indx = i2c_list.index(module)
                sensor_list.append(module)
            except ValueError:
                pass
        return sensor_list

    else:
        return i2c_list