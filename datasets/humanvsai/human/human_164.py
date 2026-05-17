def leave_swarm(self, force=False):
        url = self._url('/swarm/leave')
        response = self._post(url, params={'force': force})
        # Ignore "this node is not part of a swarm" error
        if force and response.status_code == http_client.NOT_ACCEPTABLE:
            return True
        # FIXME: Temporary workaround for 1.13.0-rc bug
        # https: 
        if force and response.status_code == http_client.SERVICE_UNAVAILABLE:
            return True
        self._raise_for_status(response)
        return True