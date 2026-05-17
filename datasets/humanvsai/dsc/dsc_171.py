class MyClass:
    def __init__(self):
        self.uid = None

    def _add_uid(self, uid, skip_handle=False):
        if not skip_handle:
            self.uid = uid
        else:
            # Handle the uid here if skip_handle is True
            pass