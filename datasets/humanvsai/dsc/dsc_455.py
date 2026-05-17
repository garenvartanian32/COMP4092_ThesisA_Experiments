class MyClass:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def get(self, key, default=None):
        """Get key value, return default if key doesn't exist"""
        return self.my_dict.get(key, default)