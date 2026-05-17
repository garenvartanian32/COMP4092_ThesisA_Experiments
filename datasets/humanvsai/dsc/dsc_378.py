import os

def extract_runscript(self):
    """
    Extract the runscript (EntryPoint) as first priority, unless the
    user has specified to use the CMD. If Entrypoint is not defined,
    we default to None:

    1. IF SREGISTRY_DOCKERHUB_CMD is set, use Cmd
    2. If not set, or Cmd is None/blank, try Entrypoint
    3. If Entrypoint is not set, use default /bin/bash
    """
    if os.getenv('SREGISTRY_DOCKERHUB_CMD'):
        return os.getenv('SREGISTRY_DOCKERHUB_CMD')
    elif self.EntryPoint:
        return self.EntryPoint
    else:
        return '/bin/bash'