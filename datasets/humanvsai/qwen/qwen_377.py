def reset(self, blocking=True):
    if blocking:
        return self._reset()
    else:
        return lambda : self._reset()