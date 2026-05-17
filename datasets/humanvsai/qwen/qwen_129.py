def get_object(cls, api_token, image_id_or_slug):
    if isinstance(image_id_or_slug, int):
        image_id = image_id_or_slug
        image_slug = None
    elif isinstance(image_id_or_slug, str):
        image_id = None
        image_slug = image_id_or_slug
    else:
        raise ValueError('image_id_or_slug must be an integer or a string')
    image_data = cls._fetch_image(api_token, image_id, image_slug)
    return cls._create_image_object(image_data)