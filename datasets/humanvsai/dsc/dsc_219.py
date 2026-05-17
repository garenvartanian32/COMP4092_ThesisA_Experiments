from astropy.io import fits
import numpy as np

def make_energies_hdu(energy_vals, extname="ENERGIES"):
    """Builds and returns a FITs HDU with the energy values

    Parameters:
    energy_vals (list): List of energy values
    extname (str): The HDU extension name

    Returns:
    hdu: FITS HDU
    """
    # Convert the list to a numpy array
    energy_array = np.array(energy_vals)

    # Create a new HDU
    hdu = fits.PrimaryHDU(energy_array)

    # Set the extension name
    hdu.header['EXTNAME'] = extname

    return hdu