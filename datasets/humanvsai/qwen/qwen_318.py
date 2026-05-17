def list_licenses():
    return ['license1', 'license2', 'license3']

def check_license_status(license_key):
    """Checks the status of a given license key"""
    if license_key in list_licenses():
        return 'Active'
    else:
        return 'Inactive'

def main():
    licenses = list_licenses()
    for license in licenses:
        status = check_license_status(license)
        print(f'License {license} is {status}')