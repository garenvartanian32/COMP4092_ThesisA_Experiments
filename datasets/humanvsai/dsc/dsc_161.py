import requests

def pypi_metadata_extension(extraction_fce):
    """Extracts data from PyPI and merges them with data from extraction
    method."""
    # Get data from PyPI
    response = requests.get('https://pypi.org/pypi/<package_name>/json')
    pypi_data = response.json()

    # Get data from extraction method
    extraction_data = extraction_fce()

    # Merge the data
    merged_data = {**pypi_data, **extraction_data}

    return merged_data