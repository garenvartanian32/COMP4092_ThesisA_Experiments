def render_message_element_as_dict(element):
    """
    Render a MessageElement as python dict
    :param element: MessageElement to render
    :type element: MessageElement
    :return: Python dict representation
    :rtype: dict
    """
    return {
        "text": element.text,
        "timestamp": element.timestamp,
        "sender": element.sender,
        "recipient": element.recipient,
        "attachments": [attachment.as_dict() for attachment in element.attachments]
    }
