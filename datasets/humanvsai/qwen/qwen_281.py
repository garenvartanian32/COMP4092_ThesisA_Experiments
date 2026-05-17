def tick(self):
    if self.queue.locked():
        raise RuntimeError('Queue is locked.')
    while not self.queue.empty():
        job = self.queue.get()
        self.submit_job(job)
        self.watch_job_progress(job)
        yield
    self.queue.task_done()