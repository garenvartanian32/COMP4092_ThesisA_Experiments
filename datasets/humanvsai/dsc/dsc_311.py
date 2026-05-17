import os
import subprocess
import tempfile

class ExampleRunner:
    def __init__(self):
        self.output = []
        self.env_vars = {}
        self.input_text = ""

    def invoke(self, command):
        # Run the command with the specified environment variables
        # and input text, and append the output to the output list
        output = subprocess.check_output(command, env=self.env_vars, text=True, input=self.input_text)
        self.output.append(output)

    def println(self, text=""):
        # Add a line of text to the output
        self.output.append(text)

    def isolated_filesystem(self):
        # Create a temporary directory and change to it
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            yield

    def run_example(self, source):
        # Run the given code, returning the lines of input and output
        exec(source, {'self': self})
        return self.output