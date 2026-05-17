def getComicData(self, comic):
    comic_data = {}
    comic_data['title'] = comic.title
    comic_data['author'] = comic.author
    comic_data['genre'] = comic.genre
    comic_data['description'] = comic.description
    comic_data['release_date'] = comic.release_date
    comic_data['rating'] = comic.rating
    comic_data['chapters'] = comic.chapters
    return comic_data