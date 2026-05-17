def _nestr(stack):
    """Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ != b$)"""
    if len(stack) < 2:
        raise ValueError("Stack must have at least two elements")

    # Pop the top two strings
    a = stack.pop()
    b = stack.pop()

    # Compare the strings
    if a != b:
        # Do something with the strings
        print(f"{a} != {b}")

# Test the function
stack = ["hello", "world", "hello", "python"]
_nestr(stack)