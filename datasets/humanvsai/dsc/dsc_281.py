import time

class JobQueue:
    def __init__(self):
        self.queue = []
        self.locked = False

    def add_job(self, job):
        if not self.locked:
            self.queue.append(job)
        else:
            raise RuntimeError("Queue is locked")

    def tick(self):
        if self.locked:
            raise RuntimeError("Queue is locked")

        while self.queue:
            job = self.queue.pop(0)
            job.start()

            while not job.is_finished():
                time.sleep(1)  # wait for 1 second

            yield job.get_result()