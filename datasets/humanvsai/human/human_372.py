def check_block_parsing(self, name, path, contents):
        if not dbt.flags.TEST_NEW_PARSER:
            return True
        try:
            dbt.clients.jinja.extract_toplevel_blocks(contents)
        except Exception:
            return False
        return True