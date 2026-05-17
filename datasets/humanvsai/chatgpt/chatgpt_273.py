import random

def compute_func(x, func, num_cases):
    sel = random.randint(0, num_cases-1)
    return func(x, sel)
