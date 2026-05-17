class JobManager:
    def __init__(self):
        self.jobs = {}  # Assume this is a dictionary where the key is the job ID and the value is the job data

    def get(self, id):
        """Retrieves the job with the selected ID.
        :param str id: The ID of the job
        :returns: The dictionary of the job if found, None otherwise"""
        return self.jobs.get(id, None)