def _get_resources(rtype='resources'):
    cpus = 0
    mem = 0
    summary = DCOSClient().get_state_summary()
    if 'slaves' in summary:
        agents = summary.get('slaves')
        for agent in agents:
            if agent[rtype].get('cpus') is not None:
                cpus += agent[rtype].get('cpus')
            if agent[rtype].get('mem') is not None:
                mem += agent[rtype].get('mem')
    return Resources(cpus, mem)