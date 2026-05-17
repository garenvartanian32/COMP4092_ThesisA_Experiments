def reset(self, blocking=True):
    promise = self.call('reset')
    if blocking:
      return promise()
    else:
      return promise