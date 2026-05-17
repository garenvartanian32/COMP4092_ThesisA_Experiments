def wait_for_armable(self, timeout=None):
        def check_armable():
            return self.is_armable
        self.wait_for(check_armable, timeout=timeout)