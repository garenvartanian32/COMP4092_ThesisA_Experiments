import re

class ReplacePattern:
    def __init__(self, search_pattern, replacement_pattern):
        self.search_pattern = search_pattern
        self.replacement_pattern = replacement_pattern

    def replace(self, nodes):
        for node in nodes:
            with open(node, 'r+') as file:
                content = file.read()
                content_new = re.sub(self.search_pattern, self.replacement_pattern, content)
                file.seek(0)
                file.write(content_new)
                file.truncate()
        return True