def open_uri(uri):
    import os
    import subprocess
    if os.name == 'nt':
        try:
            subprocess.run(['cmd.exe', '/c', 'start', uri], check=True)
        except subprocess.CalledProcessError:
            raise RuntimeError('Failed to open URI on Windows.')
    elif os.name == 'posix':
        try:
            subprocess.run(['gvfs-open', uri], check=True)
        except subprocess.CalledProcessError:
            try:
                subprocess.run(['xdg-open', uri], check=True)
            except subprocess.CalledProcessError:
                raise RuntimeError('Failed to open URI on POSIX system.')
    else:
        raise RuntimeError('Unsupported operating system.')