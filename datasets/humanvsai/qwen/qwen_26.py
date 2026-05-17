def parameters(self):
    return [self.param1, self.param2, self.param3]

def execute_tasks(self):
    """Execute tasks based on the parameters."""
    for params in self.parameters():
        self.execute_task(*params)

def execute_task(self, param1, param2, param3):
    """Execute a single task with given parameters."""
    print(f'Executing task with parameters: {param1}, {param2}, {param3}')

class TaskExecutor:

    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
    parameters = parameters
    execute_tasks = execute_tasks
    execute_task = execute_task
executor = TaskExecutor(10, 20, 30)