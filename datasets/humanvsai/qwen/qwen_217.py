def get_inventory_temp_file(self, keys=None):
    import tempfile
    import json
    with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp_file:
        inventory = self.get_inventory(keys)
        json.dump(inventory, temp_file)
        temp_file.flush()
        yield temp_file