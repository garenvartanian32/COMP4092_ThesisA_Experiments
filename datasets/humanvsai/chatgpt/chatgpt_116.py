import os

def parse_directory_tree(root_dir):
    """
    Given a root directory, returns a list of all files and subdirectories in the directory tree.
    """
    tree = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            tree.append(os.path.join(dirpath, dirname))
        for filename in filenames:
            tree.append(os.path.join(dirpath, filename))
    return tree
