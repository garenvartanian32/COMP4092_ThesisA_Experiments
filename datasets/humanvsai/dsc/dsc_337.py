import logging

def log_formatter(request=None):
    """Log formatter used in our syslog

    :param request: a request object
    :returns: logging.Formatter"""

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return formatter