def get_active_length(self):
    active_lengths = []
    for pianoroll in self.pianorolls:
        last_nonzero_index = pianoroll.shape[0] - 1
        while last_nonzero_index >= 0 and (not pianoroll[last_nonzero_index].any()):
            last_nonzero_index -= 1
        active_length = last_nonzero_index + 1
        active_lengths.append(active_length)
    return max(active_lengths)