def getComicData(self, comic):
    """Return dictionary with comic info."""
    if not isinstance(comic, dict):
        raise ValueError("comic must be a dictionary")

    # Assuming comic dictionary has keys 'title', 'author', 'year', 'publisher'
    comic_info = {
        'title': comic.get('title'),
        'author': comic.get('author'),
        'year': comic.get('year'),
        'publisher': comic.get('publisher'),
    }

    return comic_info