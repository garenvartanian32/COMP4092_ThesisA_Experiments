class Image:
    def __init__(self, image_id, slug):
        self.id = image_id
        self.slug = slug
        
class MyClass:
    @classmethod
    def get_image(cls, identifier):
        if isinstance(identifier, int):
            # assume identifier is image id
            return Image(image_id=identifier, slug=None)
        elif isinstance(identifier, str):
            # assume identifier is image slug
            return Image(image_id=None, slug=identifier)
        else:
            raise ValueError('Invalid identifier type. Must be int or str.')
