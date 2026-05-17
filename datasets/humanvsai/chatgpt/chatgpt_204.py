@staticmethod
def timestamp_record_length(time_flags: int) -> int:
    return 38 if time_flags & 0x04 else 33
