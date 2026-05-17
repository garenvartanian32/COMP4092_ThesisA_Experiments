import re

def normalize_string(input_string, separator):
    # Remove non-alpha characters
    input_string = re.sub('[^a-zA-Z]+', '', input_string)

    # Convert spaces to separator character
    input_string = input_string.replace(' ', separator)

    # Return normalized string
    return input_string
