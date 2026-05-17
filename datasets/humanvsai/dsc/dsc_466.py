def get_index_by_id(self, id):
    """Give the index associated with a given vertex id."""
    for i, vertex in enumerate(self.vertices):
        if vertex.id == id:
            return i
    return -1  # Return -1 if the id is not found