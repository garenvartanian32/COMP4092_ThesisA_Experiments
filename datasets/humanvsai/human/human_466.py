def get_index_by_id(self, id):
        for i in range(len(self.vertices)):
            if self.vertices[i].id == id:
                return i
        raise ValueError('Reverse look up of id failed.')