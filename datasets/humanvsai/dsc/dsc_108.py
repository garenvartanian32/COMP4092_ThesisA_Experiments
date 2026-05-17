def trim_phonetics(root):
    """Function that trims phonetic markup from the root.

    Parameters
    ----------
    root: str
        The string to remove the phonetic markup.

    Returns
    -------
    str
        The string with phonetic markup removed.
    """
    import re

    # Use regular expression to find and remove phonetic markup
    root = re.sub(r'\[.*?\]', '', root)

    return root