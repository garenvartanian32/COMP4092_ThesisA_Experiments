def get_url_path(self, language=None):
    """Return the URL's path component. Add the language prefix if
        ``PAGE_USE_LANGUAGE_PREFIX`` setting is set to ``True``.

        :param language: the wanted url language."""
    from settings import PAGE_USE_LANGUAGE_PREFIX
    if PAGE_USE_LANGUAGE_PREFIX:
        if language is None:
            language = self.get_language()
        if not language:
            raise ValueError('Language cannot be None or an empty string.')
        return f'/{language}{self.path}'
    return self.path