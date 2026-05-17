from typing import List
from datetime import datetime
from django.db.models.query import QuerySet

def retrieve_updated_memberships(since_when: datetime, limit_to: int, max_depth: int) -> List:
    memberships = []
    queryset = Membership.objects.filter(updated_at__gte=since_when)
    depth = 0
    while queryset.exists() and depth < max_depth:
        memberships += list(queryset[:limit_to])
        queryset = queryset[limit_to:]
        depth += 1
    return memberships
