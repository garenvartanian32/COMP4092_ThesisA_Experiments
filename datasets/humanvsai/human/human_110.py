def get_coord_system_name(header):
    try:
        ctype = header['CTYPE1'].strip().upper()
    except KeyError:
        try:
            # see if we have an "RA" header
            ra = header['RA']  # noqa
            try:
                equinox = float(header['EQUINOX'])
                if equinox < 1984.0:
                    radecsys = 'FK4'
                else:
                    radecsys = 'FK5'
            except KeyError:
                radecsys = 'ICRS'
            return radecsys.lower()
        except KeyError:
            return 'raw'
    match = re.match(r'^GLON\-.*$', ctype)
    if match:
        return 'galactic'
    match = re.match(r'^ELON\-.*$', ctype)
    if match:
        return 'ecliptic'
    match = re.match(r'^RA\-\-\-.*$', ctype)
    if match:
        hdkey = 'RADECSYS'
        try:
            radecsys = header[hdkey]
        except KeyError:
            try:
                hdkey = 'RADESYS'
                radecsys = header[hdkey]
            except KeyError:
                # missing keyword
                # RADESYS defaults to IRCS unless EQUINOX is given
                # alone, in which case it defaults to FK4 prior to 1984
                # and FK5 after 1984.
                try:
                    equinox = float(header['EQUINOX'])
                    if equinox < 1984.0:
                        radecsys = 'FK4'
                    else:
                        radecsys = 'FK5'
                except KeyError:
                    radecsys = 'ICRS'
        radecsys = radecsys.strip()
        return radecsys.lower()
    match = re.match(r'^HPLN\-.*$', ctype)
    if match:
        return 'helioprojective'
    match = re.match(r'^HGLT\-.*$', ctype)
    if match:
        return 'heliographicstonyhurst'
    match = re.match(r'^PIXEL$', ctype)
    if match:
        return 'pixel'
    match = re.match(r'^LINEAR$', ctype)
    if match:
        return 'pixel'
    #raise WCSError("Cannot determine appropriate coordinate system from FITS header")  # noqa
    return 'icrs'