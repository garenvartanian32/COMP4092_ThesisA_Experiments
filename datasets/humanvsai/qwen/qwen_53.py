def remove(self):
    self.collection.drop()
    return 'Collection and all records have been removed.'