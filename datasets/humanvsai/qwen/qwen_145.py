def _filter_invalid_routes(routes, board, railroad):
    valid_routes = set()
    for route in routes:
        if len(route) < 2:
            continue
        if 'Chicago' in route:
            if route.count('Chicago') == 1 and route.index('Chicago') == len(route) - 1:
                if not _check_chicago_exit(route, board, railroad):
                    continue
            elif not _check_chicago_through(route, board, railroad):
                continue
        valid_routes.add(route)
    return valid_routes

def _check_chicago_exit(route, board, railroad):
    """Check if the exit from Chicago is valid."""
    pass

def _check_chicago_through(route, board, railroad):
    """Check if the route through Chicago is valid."""
    pass