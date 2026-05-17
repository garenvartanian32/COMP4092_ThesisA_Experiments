import random

def _apply_with_random_selector(x, func, num_cases):
    sel = random.randint(0, num_cases-1)
    return func(x, sel)