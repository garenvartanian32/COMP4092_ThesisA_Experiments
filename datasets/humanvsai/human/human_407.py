def newDevice(deviceJson, lupusec):
    type_tag = deviceJson.get('type')
    if not type_tag:
        _LOGGER.info('Device has no type')
    if type_tag in CONST.TYPE_OPENING:
        return LupusecBinarySensor(deviceJson, lupusec)
    elif type_tag in CONST.TYPE_SENSOR:
        return LupusecBinarySensor(deviceJson, lupusec)
    elif type_tag in CONST.TYPE_SWITCH:
        return LupusecSwitch(deviceJson, lupusec)
    else:
        _LOGGER.info('Device is not known')
    return None