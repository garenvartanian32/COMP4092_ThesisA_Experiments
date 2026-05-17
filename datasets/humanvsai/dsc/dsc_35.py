class HelicalHelix:
    def __init__(self, helix_id):
        self.helix_id = helix_id

class CoiledCoil:
    def __init__(self, helices):
        self.helices = helices

    @classmethod
    def from_polymers(cls, polymers):
        helices = [HelicalHelix(i) for i in polymers]
        return cls(helices)