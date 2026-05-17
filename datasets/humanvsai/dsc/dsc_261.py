import logging

class MyClass:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def separator(self, level=None):
        """Prints a separator to the log. This can be used to separate blocks of log messages.

        The separator will default its log level to the level of the last message printed unless
        specified with the level= kwarg.

        The length and type of the separator string is determined
        by the current style. See ``setStyle``"""

        if level is None:
            level = self.logger.getEffectiveLevel()

        separator_string = "=" * 80
        self.logger.log(level, separator_string)