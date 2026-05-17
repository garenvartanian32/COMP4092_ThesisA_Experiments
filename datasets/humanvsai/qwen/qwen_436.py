def set(self, key, value, confidence=100):
    if key in self.data:
        if self.data[key]['value'] == value:
            if self.data[key]['confidence'] < confidence:
                self.data[key]['confidence'] = confidence
        elif self.data[key]['confidence'] < confidence:
            self.data[key]['value'] = value
            self.data[key]['confidence'] = confidence
    else:
        self.data[key] = {'value': value, 'confidence': confidence}