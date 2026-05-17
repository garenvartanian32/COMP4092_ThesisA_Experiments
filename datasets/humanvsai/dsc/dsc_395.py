def _ensure_valid_record_size(self, size):
    """Validate that the record size isn't too large."""
    MAX_RECORD_SIZE = 1024  # Define your maximum size here
    if size > MAX_RECORD_SIZE:
        raise ValueError("Record size is too large")