def metadata(self):
    if self._info is None:
      try:
        self._info = self._api.buckets_get(self._name)
      except Exception as e:
        raise e
    return BucketMetadata(self._info) if self._info else None