class Link:
    def __init__(self, appname, **kwargs):
        self.appname = appname
        self.options = kwargs

def create(appname, **kwargs):
    """Create a `Link` of a particular class, using the kwargs as options"""
    return Link(appname, **kwargs)