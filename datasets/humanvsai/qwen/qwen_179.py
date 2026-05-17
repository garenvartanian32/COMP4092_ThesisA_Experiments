def _read(self):
    with open(self.json_file, 'r') as file:
        try:
            compressed_data = file.read()
            decompressed_data = zlib.decompress(compressed_data)
            self.backup_dict = json.loads(decompressed_data)
        except (zlib.error, json.JSONDecodeError):
            self.backup_dict = {}