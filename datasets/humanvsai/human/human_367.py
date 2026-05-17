def call(self, method, *args, **kw):
        if args and kw:
            raise ValueError("JSON-RPC method calls allow only either named or positional arguments.")
        if not method:
            raise ValueError("JSON-RPC method call requires a method name.")
        request = self._data_serializer.assemble_request(
            method, args or kw or None
        )
        if self._in_batch_mode:
            self._requests.append(request)
            return request.get('id')
        else:
            return request