class ApplicationPolicy:
    def __init__(self, principals, actions):
        self.principals = principals
        self.actions = actions

    def validate(self):
        if not isinstance(self.principals, list) or not all(isinstance(principal, str) for principal in self.principals):
            raise InvalidApplicationPolicyError("Principals must be a list of strings")

        if not isinstance(self.actions, list) or not all(isinstance(action, str) for action in self.actions):
            raise InvalidApplicationPolicyError("Actions must be a list of strings")

        return True