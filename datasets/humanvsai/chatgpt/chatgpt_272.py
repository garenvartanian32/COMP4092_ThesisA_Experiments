def search_publications(query):
    if not isinstance(query, DBArchive):
        raise InvalidType("Invalid type. Query should be an instance of DBArchive")
    matching_archives = []
    for archive in archives:
        if (query.isbn is None or archive.isbn == query.isbn) and
           (query.title is None or archive.title == query.title) and
           (query.author is None or archive.author == query.author) and
           (query.year is None or archive.year == query.year):
            matching_archives.append(archive)
    return matching_archives