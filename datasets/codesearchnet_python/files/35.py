def _get_spill_dir(self, n):
        """ Choose one directory for spill by number n """
        return os.path.join(self.localdirs[n % len(self.localdirs)], str(n))