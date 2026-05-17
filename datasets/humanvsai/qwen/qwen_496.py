def _paramf16(ins):
    fixed_point = int(ins * 2 ** 16)
    stack.append(fixed_point)

def _paramf32(ins):
    """Pushes 32bit floating point param into the stack"""
    float_point = struct.pack('f', ins)
    stack.append(float_point)

def _parami32(ins):
    """Pushes 32bit integer param into the stack"""
    integer = int(ins)
    stack.append(integer)

def _paramu32(ins):
    """Pushes 32bit unsigned integer param into the stack"""
    unsigned_integer = int(ins) & 4294967295
    stack.append(unsigned_integer)

def _paramf64(ins):
    """Pushes 64bit floating point param into the stack"""
    double_point = struct.pack('d', ins)
    stack.append(double_point)

def _parami64(ins):
    """Pushes 64bit integer param into the stack"""
    integer = int(ins)
    stack.append(integer)

def _paramu64(ins):
    """Pushes 64bit unsigned integer param into the stack"""
    unsigned_integer = int(ins) & 18446744073709551615
    stack.append(unsigned_integer)

def _paramstr(ins):
    """Pushes string param into the stack"""
    string = str(ins)
    stack.append(string)