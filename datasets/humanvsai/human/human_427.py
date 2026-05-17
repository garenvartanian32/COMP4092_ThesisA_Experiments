def _nestr(ins):
    (tmp1, tmp2, output) = _str_oper(ins.quad[2], ins.quad[3])
    output.append('call __STRNE')
    output.append('push af')
    REQUIRES.add('string.asm')
    return output