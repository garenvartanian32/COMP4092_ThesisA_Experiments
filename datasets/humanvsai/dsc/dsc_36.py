class OutletLink:
    def __init__(self, sequence):
        self.sequence = sequence

    def update_sequence(self, new_sequence):
        self.sequence = new_sequence

# Usage
outlet_link = OutletLink([])
outlet_link.update_sequence([1, 2, 3, 4, 5])