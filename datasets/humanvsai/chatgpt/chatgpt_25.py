import signal
import sys

def handle_signal():
    if sys.platform == 'win32':
        return

    def signal_handler(sig, frame):
        sys.exit(0)

    signal.signal(signal.SIGPIPE, signal_handler)
