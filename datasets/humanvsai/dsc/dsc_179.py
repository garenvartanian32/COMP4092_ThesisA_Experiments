import json
import gzip

class BackupReader:
    def __init__(self, json_file):
        self.json_file = json_file
        self.backup_dict = {}

    def _read(self):
        try:
            with gzip.open(self.json_file, 'rt') as f:
                self.backup_dict = json.load(f)
        except (json.JSONDecodeError, gzip.BadGzipFile, FileNotFoundError):
            self.backup_dict = {}