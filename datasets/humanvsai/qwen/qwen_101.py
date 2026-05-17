def find_characteristic(self, uuid):
    for characteristic in self.characteristics:
        if characteristic.uuid == uuid:
            return characteristic
    return None