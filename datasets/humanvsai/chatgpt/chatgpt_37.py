def mangle_string(input_string):
    # Define a dictionary of non-supported characters and their corresponding ascii codes
    non_supported_chars = {'ä': 'a|', 'ö': 'o|', 'ü': 'u|', 'ß': 'ss'}
    # Replace all non-supported characters with their corresponding ascii codes
    for char, code in non_supported_chars.items():
        input_string = input_string.replace(char, code)
    # Return the updated string
    return input_string