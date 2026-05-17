def get(self, sid):
        return IncomingPhoneNumberContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )