import os

def get_symbolic_link_paths(base_dir, issuer_did=None):
    """
    Returns set of all paths to symbolic links (rev reg ids) associating their
    respective tails files, in specified base tails directory recursively
    (omitting the .hopper subdirectory), on input issuer DID if specified.
    :param base_dir: base directory for tails files, thereafter split by cred def id
    :param issuer_did: issuer DID of interest
    :return: set of paths to symbolic links associating tails files
    """
    paths = set()
    for root, dirs, files in os.walk(base_dir):
        if '.hopper' in dirs:
            dirs.remove('.hopper')
        for file in files:
            if os.path.islink(os.path.join(root, file)):
                link_target = os.readlink(os.path.join(root, file))
                if issuer_did is not None and issuer_did not in link_target:
                    continue
                paths.add(os.path.join(root, file))
    return paths
