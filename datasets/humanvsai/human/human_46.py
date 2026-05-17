def media(self):
        media = self._get_common_media()
        media += self._get_view_media()
        media += self.get_media_assets()
        return media