def get_index_by_id(self, id):
    for (index, vertex) in enumerate(self.vertices):
        if vertex.id == id:
            return index
    return -1