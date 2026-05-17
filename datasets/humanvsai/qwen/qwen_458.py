def _mul8(ins):
    a = ins.pop()
    b = ins.pop()
    if a == 0 or b == 0:
        ins.append(0)
        return
    if a == 1:
        ins.append(b)
        return
    if b == 1:
        ins.append(a)
        return
    result = a * b
    ins.append(result)
stack = [3, 4, 5]