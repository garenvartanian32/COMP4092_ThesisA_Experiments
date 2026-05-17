def retrieve_job_by_id(id):
    jobs = [
        {'id': '1', 'title': 'Job 1', 'description': 'This is the description for Job 1'},
        {'id': '2', 'title': 'Job 2', 'description': 'This is the description for Job 2'},
        {'id': '3', 'title': 'Job 3', 'description': 'This is the description for Job 3'}
    ]
    for job in jobs:
        if job['id'] == id:
            return job
    return None
