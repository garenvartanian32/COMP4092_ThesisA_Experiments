import tempfile

class InventoryManager:
    def __init__(self, keys=None):
        self.keys = keys

    def __enter__(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        return self.temp_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.temp_file.close()
        os.remove(self.temp_file.name)

# Usage
with InventoryManager() as inventory:
    # Write to the temp file
    inventory.write(b'Some inventory data')
    inventory.flush()

    # The temp file will be deleted here