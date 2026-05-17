def separator(self, *args, **kwargs):
        levelOverride = kwargs.get('level') or self._lastlevel
        self._log(levelOverride, '', 'separator', args, kwargs)