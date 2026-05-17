def media(self):
    media = super().media
    for form in self.get_forms():
        media += form.media
    return media