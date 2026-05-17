def query_paths():
    """Query paths from the PFS.

    Send a request to the /paths endpoint of the PFS specified in service_config, and
    retry in case of a failed request if it makes sense.
    """
    # Your code here