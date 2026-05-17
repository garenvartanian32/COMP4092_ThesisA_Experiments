def get_max_active_length(pianorolls):
    max_active_length = 0
    for pianoroll in pianorolls:
        active_length = 0
        for time_step in reversed(range(pianoroll.shape[0])):
            if not any(pianoroll[time_step]):
                break
            active_length += 1
        if active_length > max_active_length:
            max_active_length = active_length
    return max_active_length
