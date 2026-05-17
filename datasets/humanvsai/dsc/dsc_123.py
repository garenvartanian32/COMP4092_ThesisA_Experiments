from urllib.parse import urlparse

class URLPath:
    PAGE_USE_LANGUAGE_PREFIX = True

    def get_url_path(self, url, language=None):
        parsed_url = urlparse(url)
        path = parsed_url.path

        if self.PAGE_USE_LANGUAGE_PREFIX and language:
            path = f'/{language}{path}'

        return path