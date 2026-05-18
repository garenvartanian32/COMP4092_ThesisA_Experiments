def atbash(txt):
	a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	z = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
	s = ''
	for i in txt:
		if i in a:
			s += z[a.index(i)]
		else:
			s += i
	return s