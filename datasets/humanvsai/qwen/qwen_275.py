def get_profile_names() -> list:
    """Return the list of profile names.

    The list of names is sorted."""
    pass

def get_default_profile() -> dict:
    """Return the default profile object."""
    pass

def get_profile(profile_name: str) -> dict:
    """Return the profile object for the given profile name."""
    pass

def set_default_profile(profile_name: str) -> None:
    """Set the default profile to the given profile name."""
    pass

def delete_profile(profile_name: str) -> None:
    """Delete the profile with the given profile name."""
    pass

def update_profile(profile_name: str, profile_data: dict) -> None:
    """Update the profile with the given profile name with the provided profile data."""
    pass

def create_profile(profile_name: str, profile_data: dict) -> None:
    """Create a new profile with the given profile name and profile data."""
    pass