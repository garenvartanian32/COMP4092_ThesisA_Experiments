def _exitOnSignal(sigName, message):
    import signal
    import sys

    def handler(signum, frame):
        print(message)
        sys.exit(0)
    try:
        signal.signal(signal.__dict__[sigName], handler)
    except (AttributeError, ValueError):
        pass

def setupSignalHandlers():
    """Sets up signal handlers for common signals."""
    _exitOnSignal('SIGINT', 'Interrupted by user')
    _exitOnSignal('SIGTERM', 'Terminated by external signal')
    _exitOnSignal('SIGPIPE', 'Broken pipe')