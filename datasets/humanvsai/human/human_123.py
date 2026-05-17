def get_url_path(self, language=None):
        if self.is_first_root():
            # this is used to allow users to change URL of the root
            # page. The language prefix is not usable here.
            try:
                return reverse('pages-root')
            except Exception:
                pass
        url = self.get_complete_slug(language)
        if not language:
            language = settings.PAGE_DEFAULT_LANGUAGE
        if settings.PAGE_USE_LANGUAGE_PREFIX:
            return reverse('pages-details-by-path',
                args=[language, url])
        else:
            return reverse('pages-details-by-path', args=[url])