def add_excludes(self, excludes):
        # type: (_BaseSourcePaths, list) -> None
        if not isinstance(excludes, list):
            if isinstance(excludes, tuple):
                excludes = list(excludes)
            else:
                excludes = [excludes]
        # remove any starting rglob spec
        excl = []
        for exc in excludes:
            tmp = pathlib.Path(exc).parts
            if tmp[0] == '**':
                if len(tmp) == 1:
                    continue
                else:
                    excl.append(str(pathlib.Path(*tmp[1:])))
            else:
                excl.append(exc)
        # check for any remaining rglob specs
        if any(['**' in x for x in excl]):
            raise ValueError('invalid exclude specification containing "**"')
        if self._exclude is None:
            self._exclude = excl
        else:
            self._exclude.extend(excl)