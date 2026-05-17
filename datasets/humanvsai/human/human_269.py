def channels_unarchive(self, *, channel: str, **kwargs) -> SlackResponse:
        self._validate_xoxp_token()
        kwargs.update({"channel": channel})
        return self.api_call("channels.unarchive", json=kwargs)