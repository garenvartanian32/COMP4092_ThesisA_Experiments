def _load(self, filename=None):
    if filename is None:
        filename = self._get_filename()
    with open(filename, 'r') as file:
        data = file.read()
    self._data = data
    self._parse_data()

def _get_filename(self):
    """Generate the filename for the Himawari AHI RSR data based on the band"""
    return f'himawari_ahi_rsr_band_{self.band}.txt'

def _parse_data(self):
    """Parse the loaded data into a usable format"""
    lines = self._data.split('\n')
    self._parsed_data = {}
    for line in lines:
        if line.strip():
            (wavelength, response) = line.split()
            self._parsed_data[float(wavelength)] = float(response)