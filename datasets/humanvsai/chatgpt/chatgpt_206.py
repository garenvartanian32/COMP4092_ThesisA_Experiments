def echo(text):
    """
    Tell the DE that we would like to echo their text. See RFC 857.
    """
    return chr(1) + text + chr(0)
