def _get_indices(self, element, labels='all', mode='or'):
    indices = []
    if labels == 'all':
        labels = self.labels.keys()
    for label in labels:
        if mode == 'or':
            indices.extend(self.labels[label])
        elif mode == 'and':
            indices.append(self.labels[label])
    return indices