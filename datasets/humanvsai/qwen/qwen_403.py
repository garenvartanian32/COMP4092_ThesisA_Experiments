def _raise_on_error(self):
    if self._exception is not None:
        raise self._exception
    try:
        yield
    except Exception as e:
        self._exception = e
        raise
    finally:
        self._close_socket()

def _close_socket(self):
    """Close the socket associated with this object."""
    if self._socket is not None:
        self._socket.close()
        self._socket = None

def _set_exception(self, exception):
    """Set an exception to be raised later."""
    self._exception = exception

def _get_exception(self):
    """Get the exception that was set."""
    return self._exception

def _clear_exception(self):
    """Clear the exception that was set."""
    self._exception = None