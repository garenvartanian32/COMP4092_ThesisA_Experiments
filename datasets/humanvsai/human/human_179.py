def _read(self):
        self.json_file.seek(0)
        try:
            data = zlib.decompress(self.json_file.read())
            self.backup_dict = json.loads(data.decode('utf-8'))
        except (EOFError, zlib.error):
            self.backup_dict = {}