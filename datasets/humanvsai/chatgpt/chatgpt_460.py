import subprocess

def call_command(command, *args):
    """Call a single command with arguments."""
    cmd = [command]
    cmd.extend(args)
    subprocess.call(cmd)
