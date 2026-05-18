def flipping_bits(n):
	return int(''.join('1' if i=='0' else '0' for i in bin(n)[2:].zfill(32)),2)