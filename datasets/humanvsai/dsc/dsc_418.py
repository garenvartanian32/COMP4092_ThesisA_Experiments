import swiftclient

def export_task(self, img, cont):
    # Create a connection to the Swift service
    conn = swiftclient.Connection(
        user='username:username',
        key='password',
        authurl='http://localhost:8080/auth',
    )

    # Check if the container exists
    try:
        conn.head_container(cont)
    except swiftclient.ClientException as e:
        if e.http_status == 404:
            raise NoSuchContainer("Container does not exist")
        else:
            raise e

    # Check if the image exists
    try:
        conn.head_object(cont, img)
    except swiftclient.ClientException as e:
        if e.http_status == 404:
            raise NotFound("Image does not exist")
        else:
            raise e

    # Export the image to the container
    with open(img, 'rb') as image_file:
        conn.put_object(cont, img, image_file)