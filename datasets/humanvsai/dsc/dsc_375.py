import subprocess
import platform

def open_uri(uri):
    """Open a URI in a platform intelligent way. On Windows this will use
    'cmd.exe /c start' and on Linux this will use gvfs-open or xdg-open
    depending on which is available. If no suitable application can be
    found to open the URI, a RuntimeError will be raised.

    .. versionadded:: 1.3.0

    :param str uri: The URI to open.
    """
    if platform.system() == 'Windows':
        subprocess.Popen(['cmd.exe', '/c', 'start', uri])
    elif platform.system() == 'Linux':
        if subprocess.call(['gvfs-open', uri]) != 0:
            if subprocess.call(['xdg-open', uri]) != 0:
                raise RuntimeError("Could not open URI")
    else:
        raise RuntimeError("Unsupported operating system")