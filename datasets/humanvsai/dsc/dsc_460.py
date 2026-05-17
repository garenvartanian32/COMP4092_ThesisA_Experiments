import subprocess

def do_command(self, command, *args):
    """Call a single command with arguments."""
    command_list = [command] + list(args)
    try:
        subprocess.check_call(command_list)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")