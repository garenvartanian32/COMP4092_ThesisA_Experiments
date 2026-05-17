def check(self, var):
        if self._class is None: self._init()
        return self._class and self._checker(var, self._class)