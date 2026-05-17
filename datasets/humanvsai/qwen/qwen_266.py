def send_message(self, *args, **kwargs):
    queued = kwargs.pop('queued', False)
    isgroup = kwargs.pop('isgroup', False)
    if queued:
        print('Message is queued')
    if isgroup:
        print('Message is sent to a group')
    return self._send_message(*args, **kwargs)