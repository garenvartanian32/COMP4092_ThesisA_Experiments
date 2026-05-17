def get_entry_points(key):
    result = {}
    for entry_point in pkg_resources.iter_entry_points(key):
        result[entry_point.name] = entry_point.load()
    return result