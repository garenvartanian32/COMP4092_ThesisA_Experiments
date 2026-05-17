def multiply_last_two(stack):
    if stack[-1] == 0 or stack[-2] == 0:
        stack = [0]
    elif stack[-1] == 1:
        pass
    elif stack[-2] == 1:
        pass
    else:
        product = stack[-1] * stack[-2]
        stack = stack[:-2] + [product]
    return stack
