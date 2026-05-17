class Image:
    @classmethod
    def get_object(cls, api_token, image_id_or_slug):
        if isinstance(image_id_or_slug, int):
            return cls.get_by_id(api_token, image_id_or_slug)
        elif isinstance(image_id_or_slug, str):
            return cls.get_by_slug(api_token, image_id_or_slug)
        else:
            raise ValueError("image_id_or_slug must be an integer or a string")