def check_extraction_successful(contents):
    try:
        # extract toplevel blocks here
        extracted_blocks = extract_toplevel_blocks(contents)
        return True
    except:
        return False
