def _fmt_res(fmt, max_res=False):
    if isinstance(fmt, list):
        if max_res:
            # Allow None
            bit_res = np.max([_fmt_res(f) for f in fmt if f is not None])
        else:
            bit_res = [_fmt_res(f) for f in fmt]
        return bit_res
    return BIT_RES[fmt]