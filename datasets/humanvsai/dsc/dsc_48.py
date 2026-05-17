import os

class Job:
    def __init__(self, task, **kwargs):
        self.task = task
        self.kwargs = kwargs

    def write_jobfile(self):
        """Write the submission script. Return the path of the script"""

        # Get the arguments
        exec_args = self.kwargs.get('exec_args', [])

        # Create the job file
        job_file = os.path.join(os.getcwd(), 'job.sh')
        with open(job_file, 'w') as f:
            f.write('#!/bin/bash\n')
            f.write(f'{self.task.executable} {" ".join(exec_args)}\n')

        return job_file