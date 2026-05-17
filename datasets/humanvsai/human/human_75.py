def render_full(self, request, lodgeit_url=None):
        app = request.app
        root_path = request.app.ps.debugtoolbar.cfg.prefix
        exc = escape(self.exception)
        summary = self.render_summary(include_title=False, request=request)
        token = request.app['debugtoolbar']['pdbt_token']
        vars = {
            'evalex': app.ps.debugtoolbar.cfg.intercept_exc == 'debug' and 'true' or 'false',
            'console': 'console',
            'lodgeit_url': lodgeit_url and escape(lodgeit_url) or '',
            'title': exc,
            'exception': exc,
            'exception_type': escape(self.exception_type),
            'summary': summary,
            'plaintext': self.plaintext,
            'plaintext_cs': re.sub('-{2,}', '-', self.plaintext),
            'traceback_id': self.id,
            'static_path': root_path + 'static/',
            'token': token,
            'root_path': root_path,
            'url': root_path + 'exception?token=%s&tb=%s' % (token, self.id),
        }
        template = app.ps.jinja2.env.get_template('debugtoolbar/exception.html')
        return template.render(app=app, request=request, **vars)