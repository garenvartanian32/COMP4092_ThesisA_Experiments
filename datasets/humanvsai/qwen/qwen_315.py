def format(self, record):
    if record.levelno == logging.DEBUG:
        color = '\x1b[34m'
    elif record.levelno == logging.INFO:
        color = '\x1b[32m'
    elif record.levelno == logging.WARNING:
        color = '\x1b[33m'
    elif record.levelno == logging.ERROR:
        color = '\x1b[31m'
    elif record.levelno == logging.CRITICAL:
        color = '\x1b[35m'
    else:
        color = '\x1b[0m'
    original_format = super().format(record)
    colored_record = f'{color}{original_format}\x1b[0m'
    return colored_record