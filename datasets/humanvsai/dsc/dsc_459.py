class MyClass:
    def __init__(self, config_tags, dynamic_tags):
        self.config_tags = config_tags
        self.dynamic_tags = dynamic_tags

    def get_effective_tags(self):
        """Return configuration tags merged with dynamically applied tags."""
        return {**self.config_tags, **self.dynamic_tags}