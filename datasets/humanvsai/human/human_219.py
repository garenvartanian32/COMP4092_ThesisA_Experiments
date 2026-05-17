def make_energies_hdu(energy_vals, extname="ENERGIES"):
    cols = [fits.Column("Energy", "D", unit='MeV', array=energy_vals)]
    hdu = fits.BinTableHDU.from_columns(cols, name=extname)
    return hdu