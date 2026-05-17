from metaknowledge import Citation

def citations(val):
    """
    Extracts a list of all the citations in the record.

    Parameters
    ----------
    val : list[str]
        The raw data from a WOS file.

    Returns
    -------
    list[metaknowledge.Citation]
        A list of Citations.
    """
    citations = []
    for item in val:
        # Assuming that each item in the list is a string representation of a citation
        citation = Citation(item)
        citations.append(citation)
    return citations