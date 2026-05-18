def is_palindrome(phrase):
    cleaned = ""

    for char in phrase.lower():
        if char.isalnum():
            cleaned += char

    return check_palindrome(cleaned, 0, len(cleaned) - 1)


def check_palindrome(text, left, right):
    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    return check_palindrome(text, left + 1, right - 1)
