import functools
import asyncio

@functools.singledispatch
def convert_yielded(yielded):
    if isinstance(yielded, list):
        return asyncio.Future()  # or any other conversion logic
    elif isinstance(yielded, dict):
        return asyncio.Future()  # or any other conversion logic
    elif isinstance(yielded, asyncio.Future):
        return yielded
    else:
        raise TypeError("Unsupported type")

# Example usage:

yielded_object = [1, 2, 3]
future = convert_yielded(yielded_object)