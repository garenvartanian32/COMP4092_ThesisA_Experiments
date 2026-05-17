def extract_runscript(self):
    use_cmd = self._get_setting('SREGISTRY_DOCKER_CMD')
    # Does the user want to use the CMD instead of ENTRYPOINT?
    commands = ["Entrypoint", "Cmd"]
    if use_cmd is not None:
        commands.reverse()
    # Parse through commands until we hit one
    for command in commands:
        cmd = self._get_config(command)
        if cmd is not None:
            break
    # Only continue if command still isn't None
    if cmd is not None:
        bot.verbose3("Adding Docker %s as Singularity runscript..."
                     % command.upper())
        # If the command is a list, join. (eg ['/usr/bin/python','hello.py']
        bot.debug(cmd)
        if not isinstance(cmd, list):
            cmd = [cmd]
        cmd = " ".join(['"%s"' % x for x in cmd])
        cmd = 'exec %s "$@"' % cmd
        cmd = "#!/bin/sh\n\n%s\n" % cmd
        return cmd
    bot.debug("CMD and ENTRYPOINT not found, skipping runscript.")
    return cmd