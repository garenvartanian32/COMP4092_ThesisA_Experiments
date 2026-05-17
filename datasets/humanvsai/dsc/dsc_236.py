import subprocess

class MyClass:
    def __init__(self, cmd):
        self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def close(self):
        """Send a close message to the external process and join it."""
        self.process.terminate()
        self.process.wait()