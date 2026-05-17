def call(self, method, *args, **kw):
    if self.batch:
        return self.batch.add(method, *args, **kw)
    else:
        return self.call_api(method, *args, **kw)