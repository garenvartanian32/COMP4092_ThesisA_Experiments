class MyClass:
    def __init__(self):
        self.characteristics = [
            {'uuid': '1234', 'name': 'Characteristic 1'},
            {'uuid': '5678', 'name': 'Characteristic 2'},
            {'uuid': '9012', 'name': 'Characteristic 3'}
        ]

    def find_characteristic(self, uuid):
        for characteristic in self.characteristics:
            if characteristic['uuid'] == uuid:
                return characteristic
        return None

# Usage
my_class = MyClass()
print(my_class.find_characteristic('5678'))  # Output: {'uuid': '5678', 'name': 'Characteristic 2'}