def copy(self, target, timeout=500):
        if self.metadata and 'encoding' in self.metadata:
            with io.open(target,'w', encoding=self.metadata['encoding']) as f:
                for line in self:
                    f.write(line)
        else:
            with io.open(target,'wb') as f:
                for line in self:
                    if sys.version < '3' and isinstance(line,unicode): #pylint: disable=undefined-variable
                        f.write(line.encode('utf-8'))
                    elif sys.version >= '3' and isinstance(line,str):
                        f.write(line.encode('utf-8'))
                    else:
                        f.write(line)