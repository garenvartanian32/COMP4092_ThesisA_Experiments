def get_active_length(self):
    max_active_length = 0
    for track in self.pianorolls:
        active_length = 0
        for step in reversed(track):
            if step == 0:
                active_length += 1
            else:
                break
        max_active_length = max(max_active_length, active_length)
    return max_active_length