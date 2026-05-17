def FALSE(classical_reg):
    warn("`FALSE a` has been deprecated. Use `MOVE a 0` instead.")
    if isinstance(classical_reg, int):
        classical_reg = Addr(classical_reg)
    return MOVE(classical_reg, 0)