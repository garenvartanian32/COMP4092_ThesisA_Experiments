def get_profile_names_and_default():
    # Assume we have a list of profile objects
    profiles = [
        {'name': 'Profile1', 'default': False},
        {'name': 'Profile2', 'default': True},
        {'name': 'Profile3', 'default': False},
    ]

    # Get the list of profile names and the default profile
    profile_names = [profile['name'] for profile in profiles]
    default_profile = next((profile for profile in profiles if profile['default']), None)

    # Sort the profile names
    profile_names.sort()

    return profile_names, default_profile