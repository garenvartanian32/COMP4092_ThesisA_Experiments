import subprocess
import sys


def open_uri(uri):
    if sys.platform.startswith('win'):
        subprocess.call(['cmd.exe', '/c', 'start', uri])
    elif sys.platform.startswith('linux'):
        try:
            subprocess.call(['gvfs-open', uri])
        except OSError:
            try:
                subprocess.call(['xdg-open', uri])
            except OSError:
                raise RuntimeError("No suitable application found to open the URI.")
    else:
        raise NotImplementedError("open_uri not implemented on this platform.")
