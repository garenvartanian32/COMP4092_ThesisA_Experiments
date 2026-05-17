def render_full(self, request, lodgeit_url=None):
    if lodgeit_url is None:
        lodgeit_url = self.get_lodgeit_url()
    context = {'traceback': self.traceback, 'lodgeit_url': lodgeit_url, 'request': request, 'title': self.title, 'description': self.description, 'version': self.version, 'timestamp': self.timestamp, 'environment': self.environment, 'frames': self.frames, 'variables': self.variables, 'source': self.source, 'filename': self.filename, 'lineno': self.lineno, 'exc_type': self.exc_type, 'exc_value': self.exc_value, 'exc_traceback': self.exc_traceback}
    return self.render_template('full.html', context)