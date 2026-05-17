def _rc_sdiff(self, src, *args):
        args = list_or_args(src, args)
        src_set = self.smembers(args.pop(0))
        if src_set is not set([]):
            for key in args:
                src_set.difference_update(self.smembers(key))
        return src_set