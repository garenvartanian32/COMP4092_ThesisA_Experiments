def list_licenses():
    KEY_PATTERN = re.compile('Key (.*)')
    keys = []
    out = __salt__['cmd.run']('/sbin/emcpreg -list')
    for line in out.splitlines():
        match = KEY_PATTERN.match(line)
        if not match:
            continue
        keys.append({'key': match.group(1)})
    return keys