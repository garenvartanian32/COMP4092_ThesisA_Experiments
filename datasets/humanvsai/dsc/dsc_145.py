def _filter_invalid_routes(routes, board, railroad):
    valid_routes = []

    for route in routes:
        if len(route) < 2:  # route must contain at least 2 cities
            continue

        if 'Chicago' in route and railroad.is_impassable(board.get_exit(route[-2], route[-1])):  # route goes through Chicago using an impassable exit
            continue

        if len(route) == 1 and route[0] == 'Chicago':  # route only contains Chicago as a station, but doesn't use the correct exit path
            continue

        valid_routes.append(route)

    return valid_routes