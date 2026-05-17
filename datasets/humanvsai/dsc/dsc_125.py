def validate_client_key(self, client_key, request):
    """Validates that supplied client key."""
    if not isinstance(client_key, str) or client_key == "":
        raise ValueError("Invalid client key")