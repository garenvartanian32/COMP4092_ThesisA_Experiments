import logging

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',  # blue
        'INFO': '\033[92m',  # green
        'WARNING': '\033[93m',  # yellow
        'ERROR': '\033[91m',  # red
        'CRITICAL': '\033[95m',  # purple
    }
    RESET = '\033[0m'

    def format(self, record):
        level_name = record.levelname
        color = self.COLORS.get(level_name, '')
        reset = self.RESET
        message = logging.Formatter.format(self, record)
        return f'{color}{message}{reset}'

# Usage
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')