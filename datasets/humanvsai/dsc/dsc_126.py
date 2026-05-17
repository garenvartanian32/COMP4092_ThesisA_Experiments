import subprocess

def check_requirements_file(req_file, skip_packages):
    """Return list of outdated requirements.

    Args:
        req_file (str): Filename of requirements file
        skip_packages (list): List of package names to ignore.
    """
    # Read the requirements file
    with open(req_file, 'r') as f:
        requirements = f.readlines()

    # Remove newline characters
    requirements = [req.strip() for req in requirements]

    # Remove packages to skip
    requirements = [req for req in requirements if req not in skip_packages]

    # Check for outdated packages
    outdated_packages = []
    for req in requirements:
        try:
            output = subprocess.check_output(['pip', 'show', req])
            output = output.decode('utf-8')
            if 'outdated' in output:
                outdated_packages.append(req)
        except subprocess.CalledProcessError:
            print(f'Package {req} not found')

    return outdated_packages