import os

def attachment_simple(self, files, parentid=None):
    """Add attachments using filenames as title

    Arguments:
    files -- One or more file paths to add as attachments
    parentid -- An optional Item ID, which will create child attachments
    """
    for file in files:
        # Get the file name from the file path
        title = os.path.basename(file)

        # Add the attachment
        # This will depend on how you're adding attachments in your system
        # It might look something like this:
        self.add_attachment(file, title, parentid)