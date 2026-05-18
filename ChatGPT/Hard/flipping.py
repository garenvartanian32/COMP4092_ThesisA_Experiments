def flipping_bits(n):
    mask = (1 << 32) - 1
    return n ^ mask