def check_block_parsing(self, name, path, contents):
    try:
        # Try to split the contents into blocks
        blocks = contents.split('\n')
        # If we got here, extraction was successful
        return True
    except Exception as e:
        # If there was an exception, extraction failed
        print(f"Failed to extract blocks: {e}")
        return False