def get_entry_points(key):
    import pkg_resources
    entry_points = pkg_resources.iter_entry_points(group=key)
    return {ep.name: ep for ep in entry_points}

def load_entry_point(entry_point):
    """Load an entry point and return the loaded object.

    entry_point (pkg_resources.EntryPoint): The entry point to load.
    RETURNS (object): The loaded object."""
    return entry_point.load()

def get_loaded_entry_points(key):
    """Get and load all entry points for a given key, returning them as a dictionary.

    key (unicode): Entry point name.
    RETURNS (dict): Loaded entry points, keyed by name."""
    entry_points = get_entry_points(key)
    return {name: load_entry_point(ep) for (name, ep) in entry_points.items()}