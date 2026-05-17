def decode(self, charset='utf-8', errors='replace'):
        return URL(
            self.scheme.decode('ascii'),
            self.decode_netloc(),
            self.path.decode(charset, errors),
            self.query.decode(charset, errors),
            self.fragment.decode(charset, errors)
        )