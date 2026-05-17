def parameters(self):
        parameters = []
        for task in self.tasks:
            parameters.extend(task.parameters)
        return parameters