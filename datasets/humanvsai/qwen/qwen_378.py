def extract_runscript(self):
    if os.environ.get('SREGISTRY_DOCKERHUB_CMD') is not None:
        return self.cmd
    elif self.entrypoint is not None:
        return self.entrypoint
    else:
        return '/bin/bash'