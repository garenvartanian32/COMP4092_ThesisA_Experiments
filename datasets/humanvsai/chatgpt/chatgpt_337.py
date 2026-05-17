import logging

def syslog_formatter(request):
    log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    formatter = logging.Formatter(log_format)
    return formatter
