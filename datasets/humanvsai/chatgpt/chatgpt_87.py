import ast

def parse_pefile_docstring(file_path):
    """
    Parse docstring from file 'pefile.py' and avoid importing
    this module directly.
    """
    with open(file_path, 'r') as f:
        source = f.read()
        module = ast.parse(source)
        for node in ast.walk(module):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'PE':
                    return node.body[0].value.s
    return None
