def get_all_memberships(since_when, limit_to=100, max_depth=10):
    """Retrieve all memberships updated since "since_when"

    Loop over queries of size limit_to until either a non-full queryset
    is returned, or max_depth is reached (used in tests). Then the
    recursion collapses to return a single concatenated list.
    """
    # Your code here