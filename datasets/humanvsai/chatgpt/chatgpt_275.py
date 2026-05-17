def get_sorted_profile_names_with_default_profile(profiles):
    """
    Returns the list of profile names and the default profile object.
    The list of names is sorted.
    """
    sorted_profile_names = sorted(profiles.keys())
    default_profile = profiles.get("default")
    return sorted_profile_names, default_profile
