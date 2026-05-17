def find_all_by_parameters(self, task_name, session=None, **task_params):
    if session is None:
        session = self.session
    query = session.query(Task).filter(Task.name == task_name)
    for (key, value) in task_params.items():
        query = query.filter(getattr(Task, key) == value)
    return query.all()