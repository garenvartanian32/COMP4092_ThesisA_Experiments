def delete(self):
        url = self._api
        return self._boolean(
            self._delete(url, headers=Release.CUSTOM_HEADERS),
            204,
            404
        )