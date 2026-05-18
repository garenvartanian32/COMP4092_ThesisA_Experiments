def encrypt(word):
    # Step 1: Reverse the input
    reversed_word = word[::-1]
    
    # Step 2: Replace vowels
    vowels = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}
    replaced = ''.join(vowels.get(c, c) for c in reversed_word)
    
    # Step 3: Add "aca" to the end
    return replaced + "aca"