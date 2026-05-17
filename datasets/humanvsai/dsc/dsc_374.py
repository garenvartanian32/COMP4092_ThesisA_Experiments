class TaskScheduler:
    def __init__(self):
        self.tasks = []  # This should be a list of your tasks

    def check(self):
        ready_tasks = [task for task in self.tasks if task.is_ready()]
        return tuple(ready_tasks) if ready_tasks else None