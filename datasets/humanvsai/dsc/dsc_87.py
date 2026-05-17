import inspect

def _read_doc():
    """
    Parse docstring from file 'pefile.py' and avoid importing
    this module directly.
    """
    pass

# Get the docstring of the function
doc_string = inspect.getdoc(_read_doc)

print(doc_string)