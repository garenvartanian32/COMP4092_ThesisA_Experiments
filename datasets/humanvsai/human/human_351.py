def update(self, status, source=None, params={}):
        "Update your status.  Returns the ID of the new post."
        params = params.copy()
        params['status'] = status
        if source:
            params['source'] = source
        return self.__parsed_post(self.__post('/statuses/update.xml', params),
            txml.parseUpdateResponse)