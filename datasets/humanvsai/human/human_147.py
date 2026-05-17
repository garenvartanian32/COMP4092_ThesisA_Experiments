def find_all(self, collection):
        obj = getattr(self.db, collection)
        result = obj.find()
        return result