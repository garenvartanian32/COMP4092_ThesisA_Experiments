class MyClass:
    def __init__(self):
        self.is_batch = False

    def call(self, method, *args, **kw):
        if self.is_batch:
            return self.request_id
        else:
            return method(*args, **kw)

    def set_batch(self, is_batch):
        self.is_batch = is_batch

    def set_request_id(self, request_id):
        self.request_id = request_id