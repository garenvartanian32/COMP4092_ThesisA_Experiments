def ra_to_deg(ra_hours, ra_minutes, ra_seconds):
    # Convert hours to degrees
    ra_degrees = ra_hours * 15

    # Convert minutes to degrees
    ra_degrees += ra_minutes / 4

    # Convert seconds to degrees
    ra_degrees += ra_seconds / 240

    return ra_degrees
