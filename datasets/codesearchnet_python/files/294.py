def _make_pretty_note(note):
    """
    Makes the note description pretty and returns a formatted string if `note` is not
    an empty string. Otherwise, returns None.

    Expected input:

        ...

    Expected output:
    **Note:**

    ...

    """

    if note != "":
        note = "\n".join(map(lambda n: n[4:], note.split("\n")))
        return "**Note:**\n%s\n" % note