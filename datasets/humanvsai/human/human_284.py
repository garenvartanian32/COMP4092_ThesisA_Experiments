def _get_storage(self):
        if self._json is None:
            self._json = Storage.objects.get(**self._kwargs).json