def _mul8(ins):
    op1, op2 = tuple(ins.quad[2:])
    if _int_ops(op1, op2) is not None:
        op1, op2 = _int_ops(op1, op2)
        output = _8bit_oper(op1)
        if op2 == 1:  # A * 1 = 1 * A = A
            output.append('push af')
            return output
        if op2 == 0:
            output.append('xor a')
            output.append('push af')
            return output
        if op2 == 2:  # A * 2 == A SLA 1
            output.append('add a, a')
            output.append('push af')
            return output
        if op2 == 4:  # A * 4 == A SLA 2
            output.append('add a, a')
            output.append('add a, a')
            output.append('push af')
            return output
        output.append('ld h, %i' % int8(op2))
    else:
        if op2[0] == '_':  # stack optimization
            op1, op2 = op2, op1
        output = _8bit_oper(op1, op2)
    output.append('call __MUL8_FAST')  # Inmmediate
    output.append('push af')
    REQUIRES.add('mul8.asm')
    return output