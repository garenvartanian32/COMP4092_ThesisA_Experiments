def pkg_config_libdirs(packages):
    import subprocess
    libdirs = []
    for package in packages:
        try:
            output = subprocess.check_output(['pkg-config', '--libs-only-L', package])
            libdirs.extend(output.decode('utf-8').strip().split())
        except subprocess.CalledProcessError:
            print(f'Package {package} not found or not installed.')
    return libdirs
packages = ['glib-2.0', 'gtk+-3.0']
libdirs = pkg_config_libdirs(packages)