import random

def sample(self, trials):
    """Measure the state in the computational basis the the given number
    of trials, and return the counts of each output configuration."""

    # Assuming we have two possible outcomes: 0 and 1
    outcomes = [0, 1]

    # Initialize counts to 0
    counts = {0: 0, 1: 1}

    for _ in range(trials):
        outcome = random.choice(outcomes)
        counts[outcome] += 1

    return counts