def _apply_with_random_selector(x, func, num_cases):
    import random
    sel = random.randint(0, num_cases - 1)
    return func(x, sel)

def _apply_with_random_selector_v2(x, func, num_cases):
    """Computes func(x, sel), with sel sampled from [0...num_cases-1].

  Args:
    x: input Tensor.
    func: Python function to apply.
    num_cases: Python int32, number of cases to sample sel from.

  Returns:
    The result of func(x, sel), where func receives the value of the
    selector as a python integer, but sel is sampled dynamically."""
    import random
    sel = random.randint(0, num_cases - 1)
    return func(x, sel)