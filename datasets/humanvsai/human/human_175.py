def widgets(self):
        customization = self.activity._json_data.get('customization')
        if customization and "ext" in customization.keys():
            return customization['ext']['widgets']
        else:
            return []