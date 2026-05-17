def subscribe(self, feedUrl):
        response = self.httpPost(
            ReaderUrl.SUBSCRIPTION_EDIT_URL,
            {'ac':'subscribe', 's': feedUrl})
        # FIXME - need better return API
        if response and 'OK' in response:
            return True
        else:
            return False