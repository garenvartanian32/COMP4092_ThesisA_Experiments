def get_all_memberships(since_when, limit_to=100, max_depth=10):
    """Retrieve all memberships updated since "since_when"

        Loop over queries of size limit_to until either a non-full queryset
        is returned, or max_depth is reached (used in tests). Then the
        recursion collapses to return a single concatenated list."""
    memberships = []
    depth = 0
    offset = 0
    while depth < max_depth:
        query = Membership.objects.filter(updated_at__gte=since_when).order_by('updated_at')[offset:offset + limit_to]
        if len(query) < limit_to:
            memberships.extend(query)
            break
        memberships.extend(query)
        offset += limit_to
        depth += 1
    return memberships