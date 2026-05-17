def update_limit_current_usage(service):
    """Determine the current usage for each limit of this service,
    and update corresponding Limit via
    :py:meth:`~.AwsLimit._add_current_usage`."""
    for limit in service.limits:
        usage = get_current_usage(limit)
        limit._add_current_usage(usage)
