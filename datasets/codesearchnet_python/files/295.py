def _make_pretty_deprecated(deprecated):
    """
    Makes the deprecated description pretty and returns a formatted string if `deprecated`
    is not an empty string. Otherwise, returns None.

    Expected input:

        ...

    Expected output:
    **Deprecated:**

    ...

    """

    if deprecated != "":
        deprecated = "\n".join(map(lambda n: n[4:], deprecated.split("\n")))
        return "**Deprecated:**\n%s\n" % deprecated