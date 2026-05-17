def _get_path(self, n):
        """ Choose one directory for spill by number n """
        d = self.local_dirs[n % len(self.local_dirs)]
        if not os.path.exists(d):
            os.makedirs(d)
        return os.path.join(d, str(n))