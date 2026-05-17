def deps_list(self):
    """Returns a list of (target, dependencies)."""
    # Assuming self.targets is a dictionary where keys are targets and values are lists of dependencies
    return [(target, self.targets[target]) for target in self.targets]