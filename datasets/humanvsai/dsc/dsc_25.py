import signal
import sys

def _exitOnSignal(sigName, message):
    """Handles a signal with sys.exit.

    Some of these signals (SIGPIPE, for example) don't exist or are invalid on
    Windows. So, ignore errors that might arise."""

    # Define a signal handler
    def signal_handler(signal, frame):
        print(message)
        sys.exit(0)

    # Set the signal handler and return the original signal handler
    return signal.signal(getattr(signal, sigName), signal_handler)