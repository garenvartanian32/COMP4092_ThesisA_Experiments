def _project_name(self):
        name = getattr(self._req.req, 'project_name', '')
        if name:
            return name
        name = getattr(self._req.req, 'name', '')
        if name:
            return safe_name(name)
        raise ValueError('Requirement has no project_name.')