import subprocess

def get_pkg_config_paths(packages):
    cmd = ['pkg-config', '--libs-only-L'] + packages
    try:
        output = subprocess.check_output(cmd).decode('utf-8').strip()
        if output == '':
            return []
        else:
            return output.split()
    except subprocess.CalledProcessError:
        return []
