def can_fire_event(user_roles):
    allowed_roles = ['admin', 'moderator', 'event_manager']
    return bool(set(user_roles).intersection(allowed_roles))
