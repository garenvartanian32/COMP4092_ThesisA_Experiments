def get_coord_system_name(header):
    if 'CTYPE1' in header and 'CTYPE2' in header:
        ctype1 = header['CTYPE1']
        ctype2 = header['CTYPE2']
        if ctype1.startswith('RA') and ctype2.startswith('DEC'):
            return 'RADEC'
        elif ctype1.startswith('GLON') and ctype2.startswith('GLAT'):
            return 'GAL'
        elif ctype1.startswith('ELON') and ctype2.startswith('ELAT'):
            return 'ECLIPTIC'
        elif ctype1.startswith('HLON') and ctype2.startswith('HLAT'):
            return 'HELIO'
        elif ctype1.startswith('SLON') and ctype2.startswith('SLAT'):
            return 'SUPERGAL'
        elif ctype1.startswith('TLON') and ctype2.startswith('TLAT'):
            return 'TANGENT'
        elif ctype1.startswith('ALON') and ctype2.startswith('ALAT'):
            return 'AZEL'
        elif ctype1.startswith('VLON') and ctype2.startswith('VLAT'):
            return 'VELA'
        elif ctype1.startswith('SLON') and ctype2.startswith('SLAT'):
            return 'SUN'
        elif ctype1.startswith('OLON') and ctype2.startswith('OLAT'):
            return 'OBSERVED'
        elif ctype1.startswith('DLON') and ctype2.startswith('DLAT'):
            return 'DYNAMICAL'
        elif ctype1.startswith('FLON') and ctype2.startswith('FLAT'):
            return 'FRAME'
        elif ctype1.startswith('X') and ctype2.startswith('Y'):
            return 'PIXEL'
        elif ctype1.startswith('U') and ctype2.startswith('V'):
            return 'UV'
        elif ctype1.startswith('Q') and ctype2.startswith('U'):
            return 'QU'
        elif ctype1.startswith('L') and ctype2.startswith('M'):
            return 'LM'
        elif ctype1.startswith('X') and ctype2.startswith('Y'):
            return 'XY'
        elif ctype1.startswith('U') and ctype2.startswith('V'):
            return 'UV'
        elif ctype1.startswith('Q') and ctype2.startswith('U'):
            return 'QU'