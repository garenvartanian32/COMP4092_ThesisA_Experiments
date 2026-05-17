class Environment:
    def __init__(self):
        self.observation = None

    def reset(self, blocking=True):
        if blocking:
            self.observation = self._get_new_observation()
            return self.observation
        else:
            return lambda: self._get_new_observation()

    def _get_new_observation(self):
        # This is where you would implement the logic to get a new observation
        # For example, you might call a function that generates a random number
        return random.randint(0, 100)