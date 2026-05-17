def free_memory(handle):
    """
    Frees the memory for the array with the given handle.
    Args:
      handle: The handle of the array whose memory should be freed. This
        handle must come from the _create_array method.
    """
    del handle
