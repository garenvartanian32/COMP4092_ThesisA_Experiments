def keyword_cipher(key, message):
	LETTERS = 'zyxwvutsrqponmlkjihgfedcba'
	LETTERS_2 = 'abcdefghijklmnopqrstuvwxyz'
	LETTERS = list(LETTERS)
	cipher = {}
	for letter in key:
		if letter in cipher.values():
			pass
		else:
			cipher[LETTERS.pop()] = letter
			LETTERS_2 = LETTERS_2.replace(letter, '')
	for letter in LETTERS_2:
		cipher[LETTERS.pop()] = letter
	return ''.join(cipher[letter] if letter in cipher else letter for letter in message)