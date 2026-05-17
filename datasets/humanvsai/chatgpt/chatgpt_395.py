def validate_record_size(record: str, max_size: int) -> bool:
    if len(record) > max_size:
        return False
    else:
        return True
