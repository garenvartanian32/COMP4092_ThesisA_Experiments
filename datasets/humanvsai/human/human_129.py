def get_object(cls, api_token, image_id_or_slug):
        if cls._is_string(image_id_or_slug):
            image = cls(token=api_token, slug=image_id_or_slug)
            image.load(use_slug=True)
        else:
            image = cls(token=api_token, id=image_id_or_slug)
            image.load()
        return image