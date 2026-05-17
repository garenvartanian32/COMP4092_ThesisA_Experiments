def check_requirements_file(req_file, skip_packages):
    import pkg_resources
    import subprocess
    with open(req_file, 'r') as file:
        requirements = file.readlines()
    parsed_requirements = [pkg_resources.Requirement.parse(req.strip()) for req in requirements]
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    outdated_packages = []
    for requirement in parsed_requirements:
        if requirement.project_name.lower() in skip_packages:
            continue
        if requirement.project_name.lower() in installed_packages:
            installed_version = installed_packages[requirement.project_name.lower()]
            latest_version = subprocess.check_output(['pip', 'show', requirement.project_name]).decode().split('\n')
            latest_version = [line for line in latest_version if 'Version:' in line][0].split(': ')[1]
            if pkg_resources.parse_version(installed_version) < pkg_resources.parse_version(latest_version):
                outdated_packages.append((requirement.project_name, installed_version, latest_version))
    return outdated_packages