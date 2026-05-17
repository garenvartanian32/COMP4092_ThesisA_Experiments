def export_task(self, img, cont):
    if not self.swift_client.get_container(cont):
        raise NoSuchContainer('Container does not exist')
    if isinstance(img, Image):
        image_id = img.id
    elif isinstance(img, str):
        image_id = img
    else:
        raise ValueError('Invalid image type')
    try:
        image_details = self.glance_client.get_image(image_id)
    except NotFound:
        raise NotFound('Image not found')
    self.swift_client.put_object(cont, image_details.name, image_details.data)
    return f'Image {image_details.name} exported to container {cont}'