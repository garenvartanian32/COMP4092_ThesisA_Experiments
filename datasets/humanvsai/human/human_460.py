def do_command(self):
        method = self.args[0]
        raw_args = self.args[1:]
        if '=' in method:
            if raw_args:
                self.parser.error("Please don't mix rTorrent and shell argument styles!")
            method, raw_args = method.split('=', 1)
            raw_args = raw_args.split(',')
        self.execute(self.open(), method, self.cooked(raw_args))