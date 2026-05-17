def format(self, record):
        level = record.levelno
        if level >= logging.CRITICAL:
            color = self.CRITICAL
        elif level >= logging.ERROR:
            color = self.ERROR
        elif level >= logging.WARNING:
            color = self.WARNING
        elif level >= logging.INFO:
            color = self.INFO
        elif level >= logging.DEBUG:
            color = self.DEBUG
        else:
            color = self.DEFAULT
        message = super().format(record)
        if record.args:
            try:
                message = message % record.args
            except TypeError:
                # this happens when the message itself has some %s symbols, as
                # in traces for tracedumps
                pass
        return color + message + self.DEFAULT