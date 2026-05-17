def _get_async_status(self, response):
        if self._is_empty(response):
            return None
        body = self._as_json(response)
        return body.get('status')