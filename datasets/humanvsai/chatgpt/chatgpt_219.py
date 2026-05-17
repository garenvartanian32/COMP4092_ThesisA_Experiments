from astropy.io import fits
import numpy as np

def build_FITS_HDU_energy_values(extname, energy_values):
    hdu = fits.PrimaryHDU(data=np.array(energy_values))
    hdu.header['EXTNAME'] = extname
    return hdu
