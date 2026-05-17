def _assemble_influence(stmt):
    """Assemble an Influence statement into text."""
    # Check if the input is a string
    if isinstance(stmt, str):
        return stmt
    else:
        return "Input is not a string"