def export_image_to_swift(img, cont):
    try:
        image_id = img.id
    except AttributeError:
        image_id = img
        
    if not glance_client.images.get(image_id):
        raise NotFound()

    if not swift_client.get_container(cont):
        raise NoSuchContainer()

    data = {'os_glance_export_location': cont}
    glance_client.images.update(image_id, **data)
