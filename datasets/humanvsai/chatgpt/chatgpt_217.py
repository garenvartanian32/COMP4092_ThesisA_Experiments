from contextlib import contextmanager
import tempfile

@contextmanager
def inventory_ctx(keys):
    with tempfile.NamedTemporaryFile(delete=True) as temp:
        yield temp
