def get_coord_system_name(header):
    """Return an appropriate key code for the axes coordinate system by
    examining the FITS header."""
    if 'CTYPE1' in header:
        ctype1 = header['CTYPE1']
        if 'RA' in ctype1 or 'HPLT' in ctype1:
            return 'FK5'
        elif 'GLON' in ctype1:
            return 'GALACTIC'
        elif 'LINEAR' in ctype1:
            return 'LINEAR'
    return 'Unknown'