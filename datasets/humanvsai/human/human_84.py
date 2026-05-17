def coastal_coords():
    coast = list()
    for tile_id in coastal_tile_ids():
        tile_coord = tile_id_to_coord(tile_id)
        for edge_coord in coastal_edges(tile_id):
            dirn = tile_edge_offset_to_direction(edge_coord - tile_coord)
            if tile_id_in_direction(tile_id, dirn) is None:
                coast.append((tile_id, dirn))
    # logging.debug('coast={}'.format(coast))
    return coast