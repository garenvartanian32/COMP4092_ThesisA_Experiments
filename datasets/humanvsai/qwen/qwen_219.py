def make_energies_hdu(energy_vals, extname='ENERGIES'):
    import astropy.io.fits as fits
    import numpy as np
    if not isinstance(energy_vals, np.ndarray):
        energy_vals = np.array(energy_vals)
    col = fits.Column(name='ENERGY', format='E', array=energy_vals)
    hdu = fits.BinTableHDU.from_columns([col], name=extname)
    return hdu