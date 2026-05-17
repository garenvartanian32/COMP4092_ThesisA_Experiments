def filter_valid_routes(routes):
    valid_routes = set()
    for route in routes:
        if len(route) < 2:
            continue
        if "Chicago" in route:
            idx = route.index("Chicago")
            if idx == 0:
                if route[1] != "South":
                    continue
            elif idx == len(route) - 1:
                if route[idx - 1] != "North":
                    continue
            else:
                if (route[idx - 1] != "North" or route[idx + 1] != "South") and \
                   (route[idx - 1] != "East" or route[idx + 1] != "West") and \
                   (route[idx - 1] != "West" or route[idx + 1] != "East"):
                    continue
        valid_routes.add(tuple(route))
    return valid_routes
