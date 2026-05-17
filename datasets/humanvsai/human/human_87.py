def _read_doc():
    if sys.version_info.major == 2:
        with open('pefile.py', 'r') as f:
            tree = ast.parse(f.read())
    else:
        with open('pefile.py', 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
    return ast.get_docstring(tree)