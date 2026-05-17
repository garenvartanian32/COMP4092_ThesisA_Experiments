import pkg_resources

def get_entry_points(key):
    entry_points = {}
    for entry_point in pkg_resources.iter_entry_points(key):
        entry_points[entry_point.name] = entry_point.load()
    return entry_points
