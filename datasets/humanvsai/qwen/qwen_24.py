def validate(self):
    if not self.principals:
        raise InvalidApplicationPolicyError('Principals cannot be empty')
    if not self.actions:
        raise InvalidApplicationPolicyError('Actions cannot be empty')
    for principal in self.principals:
        if not isinstance(principal, str):
            raise InvalidApplicationPolicyError('Each principal must be a string')
        if not principal.startswith('arn:'):
            raise InvalidApplicationPolicyError('Each principal must be an ARN')
    for action in self.actions:
        if not isinstance(action, str):
            raise InvalidApplicationPolicyError('Each action must be a string')
        if not action.startswith('app:'):
            raise InvalidApplicationPolicyError("Each action must start with 'app:'")
    return True