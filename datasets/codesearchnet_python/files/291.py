def _make_pretty_usage(usage):
    """
    Makes the usage description pretty and returns a formatted string if `usage`
    is not an empty string. Otherwise, returns None.
    """

    if usage is not None and usage.strip() != "":
        usage = "\n".join(map(lambda u: u.strip(), usage.split("\n")))
        return "%s\n\n" % usage