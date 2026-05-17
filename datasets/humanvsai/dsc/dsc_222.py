class RecordStore:
    def __init__(self):
        self.records = []

    def add_record(self, schema):
        self.records.append(schema)

# Usage
store = RecordStore()
store.add_record("Person")
store.add_record("Book")
print(store.records)  # Outputs: ['Person', 'Book']