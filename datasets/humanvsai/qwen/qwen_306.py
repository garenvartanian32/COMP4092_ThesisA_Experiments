def _get_indices(self, element, labels='all', mode='or'):
    if labels is 'all':
        labels = self.labels()
    if mode == 'or':
        indices = np.where(np.any([self._get_label_indices(label) for label in labels], axis=0))[0]
    elif mode == 'and':
        indices = np.where(np.all([self._get_label_indices(label) for label in labels], axis=0))[0]
    elif mode == 'xor':
        indices = np.where(np.logical_xor.reduce([self._get_label_indices(label) for label in labels]))[0]
    elif mode == 'xnor':
        indices = np.where(np.logical_not(np.logical_xor.reduce([self._get_label_indices(label) for label in labels])))[0]
    elif mode == 'not':
        indices = np.where(np.all([np.logical_not(self._get_label_indices(label)) for label in labels], axis=0))[0]
    else:
        raise ValueError(f'Invalid mode: {mode}')
    return indices