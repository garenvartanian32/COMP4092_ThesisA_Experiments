def log_formatter(request=None):
    if request:
        return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(request_id)s')
    else:
        return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def setup_logging():
    """Setup logging configuration"""
    logger = logging.getLogger('my_logger')
    handler = logging.StreamHandler()
    formatter = log_formatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

def log_request(request):
    """Log a request with its request_id

    :param request: a request object
    :returns: None"""
    logger = logging.getLogger('my_logger')
    formatter = log_formatter(request)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Handling request', extra={'request_id': request.request_id})

def main():
    request = type('Request', (object,), {'request_id': '12345'})()
    setup_logging()
    log_request(request)