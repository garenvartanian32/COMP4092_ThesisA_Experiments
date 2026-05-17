def _rc_sdiff(self, src, *args):
    if not args:
        return self._rc_smembers(src)
    result = self._rc_smembers(src)
    for arg in args:
        result -= self._rc_smembers(arg)
    return result