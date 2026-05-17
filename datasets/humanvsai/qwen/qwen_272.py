def search_archives(query):
    if not isinstance(query, DBArchive):
        raise InvalidType('The query must be an instance of DBArchive')
    matching_archives = []
    for archive in storage_handler.get_all_archives():
        matches = True
        for (attr, value) in query.__dict__.items():
            if value is not None:
                if getattr(archive, attr, None) != value:
                    matches = False
                    break
        if matches:
            matching_archives.append(archive)
    return matching_archives