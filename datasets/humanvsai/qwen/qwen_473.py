def nworker(data, chunk):
    engine = Engine()
    engine.start()
    for i in range(0, len(data), chunk):
        chunk_data = data[i:i + chunk]
        engine.submit(jit_func, chunk_data)
    engine.stop()
    return engine.results()

def jit_func(data):
    """Function to be JIT compiled and executed on the engine."""
    result = 0
    for item in data:
        result += item
    return result

class Engine:

    def __init__(self):
        self.results = []
        self.tasks = []

    def start(self):
        """Starts the engine."""
        pass

    def stop(self):
        """Stops the engine."""
        pass

    def submit(self, func, data):
        """Submits a task to the engine."""
        self.tasks.append((func, data))

    def results(self):
        """Returns the results of all tasks."""
        for task in self.tasks:
            (func, data) = task
            self.results.append(func(data))
        return self.results
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk = 3