import os
import sys
import tempfile
import io


class CommandRunner:
    def __init__(self):
        self._output = io.StringIO()

    def invoke(self, command, env=None, input=None):
        if env is None:
            env = {}
        if input is not None:
            if isinstance(input, str):
                input = input.encode('utf-8')
            elif isinstance(input, bytes):
                pass
            else:
                raise TypeError(f'Unsupported type : {type(input)}')
        process_env = os.environ.copy()
        process_env.update(env)
        self._output.write(f'>>> {command}\n')
        process = subprocess.Popen(
            command,
            env=process_env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate(input=input)
        out = out.decode('utf-8', errors='ignore')
        err = err.decode('utf-8', errors='ignore')
        self._output.write(out)
        self._output.write(err)
        return out, err

    def println(self, text=""):
        self._output.write(text + '\n')

    def __enter__(self):
        self._old_cwd = os.getcwd()
        self._temp_dir = tempfile.TemporaryDirectory()
        os.chdir(self._temp_dir.name)
        return self

    def __exit__(self, type, value, traceback):
        os.chdir(self._old_cwd)
        self._temp_dir.cleanup()

    def get_output(self):
        return self._output.getvalue()


# Sample usage
if __name__ == '__main__':
    with CommandRunner() as runner:
        runner.println("Starting the test...")
        with runner.isolated_filesystem():
            with open('test.txt', 'w') as f:
                f.write('hello world!')
            out, err = runner.invoke('cat test.txt')
            runner.println(out.strip())
            runner.println("The test is complete!")
        output = runner.get_output()
        print(output)
