import os

def get_project_path(package):
    return os.path.abspath(os.path.dirname(package.__file__))
