def push_fixed_point_param(param):
    stack.append(int(param * (2 ** 16)))  # Multiply the param by 2^16 and cast to integer before appending to the stack
