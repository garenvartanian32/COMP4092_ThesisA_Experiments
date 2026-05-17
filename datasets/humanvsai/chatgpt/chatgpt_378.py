import os

def extract_runscript():
    cmd = os.environ.get('SREGISTRY_DOCKERHUB_CMD')
    entrypoint = None

    if cmd is not None and cmd.strip():
        return cmd
    elif entrypoint is not None and entrypoint.strip():
        return entrypoint
    else:
        return '/bin/bash'
