def check_policy_format(principals, actions):
    if not isinstance(principals, list) or not isinstance(actions, list):
        raise InvalidApplicationPolicyError('Invalid format for principals or actions')
    for p in principals:
        if not isinstance(p, str):
            raise InvalidApplicationPolicyError('Invalid format for principals')
    for a in actions:
        if not isinstance(a, str):
            raise InvalidApplicationPolicyError('Invalid format for actions')
    return True
