def read(self, size=1024):
        try:
            s = self.fileobj.read1(size)
        except (OSError, IOError) as err:
            if err.args[0] == errno.EIO:
                # Linux-style EOF
                self.flag_eof = True
                raise EOFError('End Of File (EOF). Exception style platform.')
            raise
        if s == b'':
            # BSD-style EOF (also appears to work on recent Solaris (OpenIndiana))
            self.flag_eof = True
            raise EOFError('End Of File (EOF). Empty string style platform.')
        return s