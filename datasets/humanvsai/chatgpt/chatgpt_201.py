def get_resource_type_summary(rtype='resources', role=None):
    resources = {}
    if rtype == 'resources':
        resources['cpu'] = sum([node['total_resources']['cpus'] for node in state_summary])
        resources['mem'] = sum([node['total_resources']['mem'] for node in state_summary])
    elif rtype == 'used_resources':
        resources['cpu'] = sum([node['used_resources']['cpus'] for node in state_summary])
        resources['mem'] = sum([node['used_resources']['mem'] for node in state_summary])
    elif rtype == 'offered_resources':
        resources['cpu'] = sum([node['offered_resources']['cpus'] for node in state_summary])
        resources['mem'] = sum([node['offered_resources']['mem'] for node in state_summary])
    elif rtype == 'reserved_resources':
        if role:
            nodes_with_role = [node for node in state_summary if role in node['reserved_resources']]
            resources['cpu'] = sum([node['reserved_resources'][role]['cpus'] for node in nodes_with_role])
            resources['mem'] = sum([node['reserved_resources'][role]['mem'] for node in nodes_with_role])
        else:
            resources['cpu'] = sum([sum([role_usage['cpus'] for role_usage in node['reserved_resources'].values()]) for node in state_summary])
            resources['mem'] = sum([sum([role_usage['mem'] for role_usage in node['reserved_resources'].values()]) for node in state_summary])
    elif rtype == 'unreserved_resources':
        resources['cpu'] = sum([node['unused_resources']['cpus'] for node in state_summary])
        resources['mem'] = sum([node['unused_resources']['mem'] for node in state_summary])
    return resources