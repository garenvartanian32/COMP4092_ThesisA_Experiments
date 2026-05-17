def expand_path(path):
    from uliweb import application
    
    def replace(m):
        txt = m.groups()[0]
        if txt == 'PROJECT':
            return application.apps_dir
        else:
            return pkg.resource_filename(txt, '')
    p = re.sub(r_expand_path, replace, path)
    return os.path.expandvars(os.path.expanduser(path))