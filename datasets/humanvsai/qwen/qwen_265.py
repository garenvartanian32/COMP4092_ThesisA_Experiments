def stream(self, report):
    for line in report:
        self.log(line)

def log(self, message):
    """Log a message to the application logs"""
    print(message)
report = ['Line 1', 'Line 2', 'Line 3']