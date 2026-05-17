import logging
from termcolor import colored

def format_log_record(record: logging.LogRecord) -> str:
    log_level = record.levelname
    msg = record.getMessage()
    colored_msg = colored(msg, 'white')
    if log_level == "ERROR":
        colored_msg = colored(msg, 'red')
    elif log_level == "WARNING":
        colored_msg = colored(msg, 'yellow')
    elif log_level == "INFO":
        colored_msg = colored(msg, 'green')
    elif log_level == "CRITICAL":
        colored_msg = colored(msg, 'magenta')
    elif log_level == "DEBUG":
        colored_msg = colored(msg, 'blue')
    return f"[{log_level}] {colored_msg}"
