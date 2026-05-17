def hmsToDeg(h, m, s):
    return (h + m / 60 + s / 3600) * 15

def degToHms(deg):
    """Convert an angle in degrees into RA hours, minutes, seconds."""
    h = int(deg / 15)
    m = int((deg / 15 - h) * 60)
    s = ((deg / 15 - h) * 60 - m) * 60
    return (h, m, s)
ra_hms = (12, 34, 56)
ra_deg = hmsToDeg(*ra_hms)
ra_deg = 189.73166666666668
ra_hms = degToHms(ra_deg)