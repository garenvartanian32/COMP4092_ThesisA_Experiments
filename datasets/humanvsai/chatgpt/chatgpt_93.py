from collections.abc import MutableMapping


def merge_headers(call_specific_headers=None):
    merged_headers = KeyCaseInsensitiveMutableMapping()
    if call_specific_headers:
        merged_headers.update(call_specific_headers)
    merged_headers.update(KeyCaseInsensitiveMutableMapping(self.headers))
    return merged_headers


class KeyCaseInsensitiveMutableMapping(MutableMapping):
    def __init__(self, init_dict=None, **kwargs):
        self._store = dict()
        if init_dict:
            self.update(init_dict)
        self.update(kwargs)

    def __len__(self):
        return len(self._store)

    def __getitem__(self, key):
        return self._store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self._store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self._store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self._store)

    def __keytransform__(self, key):
        return str(key).lower()
