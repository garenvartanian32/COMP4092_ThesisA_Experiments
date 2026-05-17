def get_key_code(fits_header):
    """
    Return an appropriate key code for the axes coordinate system
    by examining the FITS header.
    """
    axis_codes = {'RA': 'CTYPE1', 'DEC': 'CTYPE2', 'Stokes': 'CTYPE3', 'Freq': 'CTYPE4'}
    for axis, code in axis_codes.items():
        if code in fits_header:
            return axis
    return None
