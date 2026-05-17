class StackUnderflowException(Exception):
    pass


def pop(stack, index=-1):
    """pop element from stack at specified index"""
    if not stack:
        raise StackUnderflowException("Cannot pop from empty stack")
    return stack.pop(index)
