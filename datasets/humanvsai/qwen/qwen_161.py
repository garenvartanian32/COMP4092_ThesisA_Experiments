def pypi_metadata_extension(extraction_fce):

    def wrapper(package_name):
        import requests
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
        if response.status_code == 200:
            pypi_data = response.json()
        else:
            raise ValueError(f'Failed to fetch data for {package_name} from PyPI')
        additional_data = extraction_fce(package_name)
        merged_data = {**pypi_data, **additional_data}
        return merged_data
    return wrapper

def example_extraction_fce(package_name):
    return {'example_key': 'example_value'}

@pypi_metadata_extension(example_extraction_fce)
def get_package_data(package_name):
    return package_name