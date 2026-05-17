def list_xattrs(self, path, **kwargs):
        return simplejson.loads(_json(self._get(path, 'LISTXATTRS', **kwargs))['XAttrNames'])