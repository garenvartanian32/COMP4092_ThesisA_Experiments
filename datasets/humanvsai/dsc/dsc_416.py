def include_file(p):
    """
    This function includes a file.

    Parameters:
    p (str): The path to the file to be included.

    Returns:
    str: The content of the file.
    """
    with open(p, 'r') as file:
        return file.read()