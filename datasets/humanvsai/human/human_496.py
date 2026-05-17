def _paramf16(ins):
    output = _f16_oper(ins.quad[1])
    output.append('push de')
    output.append('push hl')
    return output