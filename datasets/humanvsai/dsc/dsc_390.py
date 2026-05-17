class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, **task_params):
        self.tasks.append({'name': task_name, 'params': task_params})

    def find_all_by_parameters(self, task_name, **task_params):
        found_tasks = []
        for task in self.tasks:
            if task['name'] == task_name and task['params'] == task_params:
                found_tasks.append(task)
        return found_tasks

# Usage
manager = TaskManager()
manager.add_task('task1', param1='value1', param2='value2')
manager.add_task('task2', param1='value3', param2='value4')

found_tasks = manager.find_all_by_parameters('task1', param1='value1', param2='value2')
print(found_tasks)  # Output: [{'name': 'task1', 'params': {'param1': 'value1', 'param2': 'value2'}}]