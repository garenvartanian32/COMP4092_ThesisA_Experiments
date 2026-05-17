import requests

def extract_and_merge_data(pypi_url, extraction_method_data):
    pypi_data = requests.get(pypi_url).json()
    merged_data = {**pypi_data, **extraction_method_data}
    return merged_data
