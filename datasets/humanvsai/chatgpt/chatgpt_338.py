def count_characters(filename):
    """
    Count the occurrences of the different characters in the file.

    :param filename: name of the file to count the characters in.
    """
    char_count = {}

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    return char_count
