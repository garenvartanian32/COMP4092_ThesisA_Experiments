def check_block_parsing(self, name, path, contents):
    try:
        self.parse_blocks(name, path, contents)
        return True
    except Exception as e:
        print(f'Failed to parse blocks for {name} at {path}: {e}')
        return False