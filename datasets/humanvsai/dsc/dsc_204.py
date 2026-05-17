def length(time_flags):
    """Static method to return the length of the Rock Ridge Time Stamp
        record.

        Parameters:
         time_flags - Integer representing the flags to use.
        Returns:
         The length of this record in bytes."""

    # The length of the record is 12 bytes for the fixed part
    length = 12

    # If the flag is set, add 4 bytes for the timezone offset
    if time_flags & 0x01:
        length += 4

    # If the flag is set, add 4 bytes for the daylight savings offset
    if time_flags & 0x02:
        length += 4

    # If the flag is set, add 4 bytes for the timezone abbreviation
    if time_flags & 0x04:
        length += 4

    # If the flag is set, add 4 bytes for the daylight savings abbreviation
    if time_flags & 0x08:
        length += 4

    return length