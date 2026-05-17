def multicall(self, viewname, fields):
        commands = tuple('d.{}='.format(x) for x in fields)
        result_type = namedtuple('DownloadItem', [x.replace('.', '_') for x in fields])
        items = self.open().d.multicall(viewname, *commands)
        return [result_type(*x) for x in items]