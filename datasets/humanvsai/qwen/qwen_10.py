def start_logging(logfile='gromacs.log'):
    import logging
    logger = logging.getLogger('gromacs')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def log_message(logger, message, level='info'):
    """Log a message with a specified level.

    Parameters:
    logger (logging.Logger): The logger object to use.
    message (str): The message to log.
    level (str): The level of the log message. Default is "info".
    """
    if level.lower() == 'debug':
        logger.debug(message)
    elif level.lower() == 'info':
        logger.info(message)
    elif level.lower() == 'warning':
        logger.warning(message)
    elif level.lower() == 'error':
        logger.error(message)
    elif level.lower() == 'critical':
        logger.critical(message)
    else:
        raise ValueError(f'Unknown log level: {level}')