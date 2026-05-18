def convert_to_hex(txt):
	x = []
	for i in txt:
		y = hex(ord(i))
		x.append(y[2:])
	return ' '.join(x)