def attachment_simple(self, files, parentid=None):
    if not files:
        return None
    if isinstance(files, str):
        files = [files]
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
        title = os.path.basename(file)
        self.add_attachment(content, title, parentid)

def add_attachment(self, content, title, parentid=None):
    """Add an attachment to an item
        Arguments:
        content: The binary content of the attachment
        title: The title of the attachment
        parentid: An optional Item ID, which will create child attachments"""
    pass