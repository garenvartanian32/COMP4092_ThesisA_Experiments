import logging

def start_logging(logfile="gromacs.log"):
    """Start logging of messages to file and console.

    The default logfile is named ``gromacs.log`` and messages are
    logged with the tag *gromacs*."""

    # Create a logger
    logger = logging.getLogger('gromacs')
    logger.setLevel(logging.DEBUG)

    # Create a file handler which logs even debug messages
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)

    # Create a console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger