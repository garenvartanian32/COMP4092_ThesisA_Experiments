def list_xattrs(self, path, **kwargs):
    return self._xattr.listxattr(path, **kwargs)