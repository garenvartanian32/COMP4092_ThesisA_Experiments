import json

class Storage:
    def __init__(self, json_data):
        self.json = json_data

    def _get_storage(self):
        """Load `json` field from `Storage` object."""
        return json.loads(self.json)