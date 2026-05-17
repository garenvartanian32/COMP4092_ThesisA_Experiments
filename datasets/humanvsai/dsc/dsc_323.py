def hmsToDeg(h, m, s):
    """Convert RA hours, minutes, seconds into an angle in degrees."""
    return 15 * (h + m / 60 + s / 3600)