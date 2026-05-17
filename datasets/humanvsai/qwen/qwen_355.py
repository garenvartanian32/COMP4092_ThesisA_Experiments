def auto_complete_paths(current, completion_type):
    import os
    import fnmatch
    if os.path.isdir(current):
        entries = os.listdir(current)
        if completion_type == 'file':
            return (os.path.join(current, entry) for entry in entries)
        elif completion_type == 'path':
            return (os.path.join(current, entry) for entry in entries)
        elif completion_type == 'dir':
            return (os.path.join(current, entry) for entry in entries if os.path.isdir(os.path.join(current, entry)))
    else:
        parent_dir = os.path.dirname(current)
        base_name = os.path.basename(current)
        entries = os.listdir(parent_dir)
        if completion_type == 'file':
            return (os.path.join(parent_dir, entry) for entry in entries if fnmatch.fnmatch(entry, base_name + '*'))
        elif completion_type == 'path':
            return (os.path.join(parent_dir, entry) for entry in entries if fnmatch.fnmatch(entry, base_name + '*'))
        elif completion_type == 'dir':
            return (os.path.join(parent_dir, entry) for entry in entries if fnmatch.fnmatch(entry, base_name + '*') and os.path.isdir(os.path.join(parent_dir, entry)))