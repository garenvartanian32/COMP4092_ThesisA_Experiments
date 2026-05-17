def submit_and_watch_jobs(queue):
    if queue.locked():
        raise RuntimeError("Queue is locked")

    for job in queue:
        submit_job(job)
        while not job.is_done():
            watch_progress(job)
        yield
