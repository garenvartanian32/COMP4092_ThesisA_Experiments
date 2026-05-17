def find_tasks_by_name(task_name, **kwargs):
    #assuming that the tasks are stored in a list called all_tasks
    filtered_tasks = [task for task in all_tasks if task['name'] == task_name and all(param in task['params'].items() for param in kwargs.items())]
    return filtered_tasks
