def _rc_sdiff(self, src, *args):
    result = set(src)
    for arg in args:
        result -= set(arg)
    return result