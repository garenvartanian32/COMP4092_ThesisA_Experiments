import json

def save_matpower(self, fd):
    """Serialize the case as a MATPOWER data file."""
    data = {
        'bus': self.bus,
        'gen': self.gen,
        'branch': self.branch,
        # add other attributes as needed
    }

    with open(fd, 'w') as f:
        json.dump(data, f)