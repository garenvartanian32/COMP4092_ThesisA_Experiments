def names2dnsrepr(x):
    if type(x) is str:
        if x and x[-1] == '\x00': # stupid heuristic
            return x.encode('ascii')
        x = [x.encode('ascii')]
    elif type(x) is bytes:
        if x and x[-1] == 0:
            return x
        x = [x]
    res = []
    for n in x:
        if type(n) is str:
            n = n.encode('ascii')
        termin = b"\x00"
        if n.count(b'.') == 0: # single-component gets one more
            termin += bytes([0]) 
        n = b"".join(map(lambda y: chr(len(y)).encode('ascii')+y, n.split(b"."))) + termin
        res.append(n)
    return b"".join(res)