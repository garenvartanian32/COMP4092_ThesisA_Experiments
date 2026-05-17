def samples_by_indices(self, indices):
    if isinstance(indices, slice):
        indices = list(range(*indices.indices(len(self.data))))
    if hasattr(self, 'index_map'):
        indices = [self.index_map[i] for i in indices]
    batch = [self.data[i] for i in indices]
    return batch