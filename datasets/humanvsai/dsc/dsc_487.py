class ShadowStore:
    def __init__(self):
        self.shadow_store = []

    def AddShadow(self, fileset):
        """Add the shadow entries to the shadow store."""
        self.shadow_store.extend(fileset)