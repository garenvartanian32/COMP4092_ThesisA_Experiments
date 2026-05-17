import logging

class ReportStreamer:
    def __init__(self):
        # Set up logging to a file
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S',
                            handlers=[logging.FileHandler('application.log'), logging.StreamHandler()])

    def stream(self, report):
        """Stream reports to application logs"""
        logging.info(report)