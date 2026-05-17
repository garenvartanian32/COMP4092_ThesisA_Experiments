def find_characteristic(self, uuid):
        for char in self.list_characteristics():
            if char.uuid == uuid:
                return char
        return None