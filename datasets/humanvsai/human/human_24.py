def validate(self):
        if not self.principals:
            raise InvalidApplicationPolicyError(error_message='principals not provided')
        if not self.actions:
            raise InvalidApplicationPolicyError(error_message='actions not provided')
        if any(not self._PRINCIPAL_PATTERN.match(p) for p in self.principals):
            raise InvalidApplicationPolicyError(
                error_message='principal should be 12-digit AWS account ID or "*"')
        unsupported_actions = sorted(set(self.actions) - set(self.SUPPORTED_ACTIONS))
        if unsupported_actions:
            raise InvalidApplicationPolicyError(
                error_message='{} not supported'.format(', '.join(unsupported_actions)))
        return True