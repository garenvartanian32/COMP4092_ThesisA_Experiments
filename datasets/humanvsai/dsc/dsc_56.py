class Entry:
    def __init__(self, source_from):
        self.source_from = source_from

def get_sourced_from(entry):
    """Get a list of values from the source_from attribute"""
    return entry.source_from