class MyClass:
    def __init__(self):
        self.status = None

    def update(self, status, source=None, params={}):
        """Update your status.  Returns the ID of the new post."""
        self.status = status
        # Your update logic here
        return new_post_id