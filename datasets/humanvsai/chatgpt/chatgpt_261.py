def print_separator(level=None):
    """
    Prints a separator to the log. This can be used to separate blocks of log messages.
    The separator will default its log level to the level of the last message printed unless
    specified with the level= kwarg.
    The length and type of the separator string is determined
    by the current style. See ``setStyle``
    """

    if level is None:
        level = logging.getLogger().last_log_level

    separator = logging.getLogger().separator_string()

    logging.log(level, separator)
