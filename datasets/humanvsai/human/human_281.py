def tick(self):
        self.on_start()
        while not self.is_empty:
            cruft = []
            for job in self.queue:
                if not self.ready(job):
                    continue
                self.on_ready(job)
                try:
                    job.submit()
                except ValueError:
                    if job.should_retry:
                        self.on_error(job)
                        job.attempts += 1
                    else:
                        self.on_fail(job)
                        cruft.append(job)
                        self.failed.append(job)
                else:
                    self.running.append(job)
                    self.on_submit(job)
                    cruft.append(job)
            self.queue = [job for job in self.queue if job not in cruft]
            cruft = []
            for job in self.running:
                if job.is_running() or job.is_queued():
                    pass
                elif job.is_complete():
                    self.on_complete(job)
                    cruft.append(job)
                    self.complete.append(job)
                elif job.is_fail():
                    self.on_fail(job)
                    cruft.append(job)
                    self.failed.append(job)
                elif job.is_error():
                    self.on_error(job)
                    cruft.append(job)
                else:
                    pass
            self.running = [job for job in self.running if job not in cruft]
            if self.locked() and self.on_locked():
                raise RuntimeError
            self.on_tick()
            yield
        self.on_end()