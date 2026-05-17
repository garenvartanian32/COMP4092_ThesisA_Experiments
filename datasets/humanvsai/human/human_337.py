def log_formatter(request=None):
    if request:
        format_str = ('%(asctime)s {ip} {name}:  ENV={env} '
                      'REMOTE_IP=%(remote_ip)s REQUEST_ID=%(request_id)s '
                      '%(message)s')
    else:
        format_str = '%(asctime)s {ip} {name}:  ENV={env} %(message)s'
    try:
        hostname = socket.gethostname()
    except socket.gaierror:
        hostname = 'localhost'
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = '127.0.0.1'
    formatter = logging.Formatter(
            format_str.format(ip=ip, name=options.name, env=options.env),
            datefmt='%Y-%m-%dT%H:%M:%S')
    logging.Formatter.converter = time.gmtime
    return formatter