def wfdb_bit_res(fmt, max_res=False):
    BIT_RES = {"212": 12, "310": 10, "311": 11, "16": 16, "24": 24}

    def get_res(fmt):
        return BIT_RES.get(fmt.upper())

    if isinstance(fmt, str):
        bit_res = get_res(fmt)
    elif max_res:
        bit_res = max([get_res(f) for f in fmt])
    else:
        bit_res = [get_res(f) for f in fmt]
    return bit_res