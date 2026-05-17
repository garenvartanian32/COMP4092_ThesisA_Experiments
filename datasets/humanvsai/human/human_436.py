def set(self, key, value, confidence=100):
        if value is None:
            return
        if key in self.info:
            old_confidence, old_value = self.info.get(key)
            if old_confidence >= confidence:
                return
        self.info[key] = (confidence, value)