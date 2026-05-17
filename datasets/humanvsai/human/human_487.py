def AddShadow(self, fileset):
    shadow = fileset.get("/etc/shadow")
    if shadow:
      self._ParseFile(shadow, self.ParseShadowEntry)
    else:
      logging.debug("No /etc/shadow file.")