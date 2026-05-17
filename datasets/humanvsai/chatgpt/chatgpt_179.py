import gzip
import json

class BackupManager:
    def __init__(self, json_file):
        self.json_file = json_file
        self.backup_dict = {}
        
    def read_backup_file(self):
        try:
            with gzip.open(self.json_file, 'rb') as f:
                file_content = f.read()
            if file_content:
                json_content = json.loads(file_content.decode('utf-8'))
                self.backup_dict = json_content
        except:
            pass
