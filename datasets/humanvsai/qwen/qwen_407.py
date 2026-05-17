def newDevice(deviceJson, lupusec):
    deviceType = deviceJson['type']
    if deviceType == 'camera':
        return Camera(deviceJson, lupusec)
    elif deviceType == 'sensor':
        return Sensor(deviceJson, lupusec)
    elif deviceType == 'light':
        return Light(deviceJson, lupusec)
    else:
        raise ValueError(f'Unsupported device type: {deviceType}')

class Camera:

    def __init__(self, deviceJson, lupusec):
        self.deviceJson = deviceJson
        self.lupusec = lupusec
        self.name = deviceJson['name']
        self.resolution = deviceJson['resolution']
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        print(f'Camera {self.name} started recording.')

    def stop_recording(self):
        self.is_recording = False
        print(f'Camera {self.name} stopped recording.')

class Sensor:

    def __init__(self, deviceJson, lupusec):
        self.deviceJson = deviceJson
        self.lupusec = lupusec
        self.name = deviceJson['name']
        self.type = deviceJson['type']
        self.is_active = True

    def activate(self):
        self.is_active = True
        print(f'Sensor {self.name} activated.')

    def deactivate(self):
        self.is_active = False
        print(f'Sensor {self.name} deactivated.')

class Light:

    def __init__(self, deviceJson, lupusec):
        self.deviceJson = deviceJson
        self.lupusec = lupusec
        self.name = deviceJson['name']
        self.brightness = deviceJson['brightness']
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f'Light {self.name} turned on with brightness {self.brightness}.')

    def turn_off(self):
        self.is_on = False
        print(f'Light {self.name} turned off.')
deviceJson = {'type': 'camera', 'name': 'Front Door Camera', 'resolution': '1080p'}
lupusec = 'some_lupusec_value'
camera = newDevice