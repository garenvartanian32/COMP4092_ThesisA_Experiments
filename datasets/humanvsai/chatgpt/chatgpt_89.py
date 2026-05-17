import os
import pkg_resources

def auto_search(path):
    if '$[' in path and ']' in path:
        start = path.index('$[') + 2
        end = path.index(']')
        var = path[start:end]
        if var == 'PROJECT':
            dir = pkg_resources.resource_filename('', '')
            path = path.replace('$[PROJECT]', dir)
        else:
            path = path.replace('$[{}]'.format(var), var)
        path = os.path.expandvars(os.path.expanduser(path))
    return path
