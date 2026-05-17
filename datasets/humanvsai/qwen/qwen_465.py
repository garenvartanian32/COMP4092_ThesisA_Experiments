def get(self, id):
    job = self.jobs.get(id)
    if job is None:
        return None
    return job