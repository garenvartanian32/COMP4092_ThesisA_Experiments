def get_effective_tags(self):
    config_tags = self.config.get('tags', {})
    dynamic_tags = self.dynamic_tags or {}
    effective_tags = {**config_tags, **dynamic_tags}
    return effective_tags