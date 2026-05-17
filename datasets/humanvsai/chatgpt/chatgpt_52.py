def replace_strings(string, search_and_replacements):
    """
    Replaces occurrences of strings in the input 'string' with the strings in the
    corresponding positions of the input 'search_and_replacements'.

    :param string: input string to be modified
    :param search_and_replacements: list of tuples, where each tuple contains
                                     two strings: the string to be found and the
                                     string to replace it with
    :return: the modified string
    """
    for old, new in search_and_replacements:
        string = string.replace(old, new)
    return string
