def get(self, sid):
    return IncomingPhoneNumberContext(self._version, self._solution, sid)